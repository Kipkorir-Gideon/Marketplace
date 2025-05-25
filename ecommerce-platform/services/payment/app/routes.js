const express = require('express');
const router = express.Router();
const { processPayment, refundPayment, getPaymentStatus } = require('./utils');

// Route to process a payment
router.post('/payment', async (req, res) => {
    try {
        const paymentResult = await processPayment(req.body);
        res.status(200).json(paymentResult);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Route to process a refund
router.post('/payment/:id/refund', async (req, res) => {
    try {
        const refundResult = await refundPayment(req.params.id);
        res.status(200).json(refundResult);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Route to get payment status
router.get('/payment/:id', async (req, res) => {
    try {
        const status = await getPaymentStatus(req.params.id);
        res.status(200).json(status);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

module.exports = router;