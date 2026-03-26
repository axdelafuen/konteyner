require 'sinatra'
require 'json'

# Logging middleware
use Rack::CommonLogger

# Define static list of ingredients with calorie values
STATIC_INGREDIENTS = [
  { ingredient: 'apple', calories: 52 },
  { ingredient: 'banana', calories: 105 },
  { ingredient: 'orange', calories: 62 },
  { ingredient: 'strawberry', calories: 4 },
  { ingredient: 'blueberry', calories: 29 },
  { ingredient: 'kiwi', calories: 61 },
  { ingredient: 'grapefruit', calories: 52 },
  { ingredient: 'pineapple', calories: 50 },
  { ingredient: 'mango', calories: 60 },
  { ingredient: 'watermelon', calories: 46 },
  { ingredient: 'peach', calories: 59 },
  { ingredient: 'pear', calories: 57 },
  # Add more ingredients and their respective calorie values as needed
].freeze

# Define routes
get '/' do
  # Prepare the response with the static list of ingredients
  response = STATIC_INGREDIENTS.map { |entry| { ingredient: entry[:ingredient], calories: entry[:calories] } }

  response.to_json
end

get '/health' do
  # Health check route, returns a simple JSON response
  { status: 'ok' }.to_json
end

# Accept port as an input variable or use the default (80)
set :port, ENV['PORT'] || 80
set :bind, '0.0.0.0'

# Start the server
Sinatra::Application.run! if $PROGRAM_NAME == __FILE__
