const express = require('express');
const { check, validationResult } = require('express-validator');
const router = express.Router();

/*
@route     api/restaurants/all
@desc      Get list of all restaurants 
@access    Public
*/
router.get(
    '/all',
    [],
    async (req, res) => {
        try {
            
            

        } catch(err) {
            console.error(err.message);
            res.status(500).send('Server Not Responding');
        }
    }
);


module.exports = router;
