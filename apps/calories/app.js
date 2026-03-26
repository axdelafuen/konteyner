const express = require("express");
const mongoose = require("mongoose");
const morgan = require("morgan");

const app = express();
const port = process.env.PORT || 80;

// Logging middleware
app.use(morgan("dev"));

// Define a MongoDB schema and model
const calorieSchema = new mongoose.Schema({
  sex: String,
  calories: Number,
});

// Attempt to connect to MongoDB
// format of connection string: mongodb://localhost:27017/your-database-name
mongoose.connect(process.env.MONGODB_CONNECTION_STRING);
const db = mongoose.connection;
const Calorie = mongoose.model(process.env.MONGODB_COLLECTION, calorieSchema);

// Check if the collection is empty, and insert default values if needed
db.once('open', async () => {
  try {
    const count = await Calorie.countDocuments();

    if (count === 0) {
      // Insert default values if the collection is empty
      await Calorie.create([
        { sex: 'man', calories: 2500 },
        { sex: 'woman', calories: 2000 },
      ]);

      console.log('Default values inserted into the', process.env.MONGODB_COLLECTION, 'collection');
    }
  } catch (error) {
    console.error('Error checking or inserting default values:', error);
  }
});

// Define the API endpoint
app.get("/", async (req, res) => {
  try {
    // Check if MongoDB is connected
    if (db.readyState !== 1) {
      res.status(500).json({ error: "MongoDB is not connected" });
      return;
    }

    // Fetch data from MongoDB
    const calories = await Calorie.find();

    if (!calories || calories.length === 0) {
      // Handle the case where no data is found in the database
      res.status(404).json({ error: "No data found" });
      return;
    }

    // Prepare the response in JSON format
    const response = {
      man: calories.find((entry) => entry.sex === "man").calories,
      woman: calories.find((entry) => entry.sex === "woman").calories,
    };

    res.json(response);
  } catch (error) {
    console.error("API error:", error);

    if (error instanceof mongoose.Error) {
      // Handle MongoDB-related errors separately
      res.status(500).json({ error: "MongoDB Error" });
    } else {
      // Handle other errors
      res.status(500).json({ error: "Internal Server Error" });
    }
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
