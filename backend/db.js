const mongoose = require('mongoose');
const config = require('config');
const mongoURI = config.get('mongoURI');

const connection = async () => {
    try {
        await mongoose.connect(
            mongoURI,
            { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true }
        );
        console.log('MongoDB Connected...');  // temporary
    } catch(err) {
        console.error(err.message);
        process.exit(1);
    }
}

module.exports = connection;