FROM ruby:2.7.1
WORKDIR /app
COPY Gemfile* ./
RUN bundle install
COPY . .
EXPOSE 80
CMD ["ruby", "ingredients.rb"]