const mongoose = require('mongoose');

const RestaurantSchema = new mongoose.Schema({
    name: {
        type: String,
    },
    rating: {
        type: String,
    },
    price: {
        type: Number,
    },
    review: {
        type: String,
    },
    dishes: [Object],
    contexts: [String],
    cuisines: [String],
    districts: [String],
});

module.exports = Restaurant = mongoose.model('restaurant', RestaurantSchema);