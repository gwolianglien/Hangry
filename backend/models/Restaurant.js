const mongoose = require('mongoose');

const RestaurantSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    rating: {
        type: Number,
        default: 0,
        required: true,
    },
    price: {
        type: Number,
    },
    review: {
        type: String,
    },
    dishes: [
        mongoose.Schema.Types.ObjectId,
    ],
    contexts: [String],
    cuisines: [String],
    districts: [String],
});

module.exports = Restaurant = mongoose.model('restaurant', RestaurantSchema);