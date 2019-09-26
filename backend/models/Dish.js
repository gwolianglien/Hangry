const mongoose = require('mongoose');

const DishSchema = new mongoose.Schema({
    name: {
        type: String,
    },
    review: {
        type: String
    }
});

module.exports = Dish = mongoose.model('dish', DishSchema);