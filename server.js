const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Set view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// BBQ Salt Calculator constants and functions
const KOSHER_SALT_MG_PER_TSP = 480;
const RECOMMENDED_SODIUM_PER_LB = 400; // mg per lb for baby back ribs
const RUB_TBSP_PER_RACK = 4;
const AVERAGE_RACK_WEIGHT = 2; // lbs

// Convert teaspoons to tablespoons (1 tbsp = 3 tsp)
const tspToTbsp = (tsp) => tsp / 3;
const tbspToTsp = (tbsp) => tbsp * 3;

// Calculate sodium from rub
function calculateRubSodium(rubSodiumPerQuarterTsp, ribWeight) {
    // Calculate how many racks based on weight
    const numberOfRacks = ribWeight / AVERAGE_RACK_WEIGHT;

    // Total tablespoons of rub needed
    const totalRubTbsp = numberOfRacks * RUB_TBSP_PER_RACK;

    // Convert to teaspoons (1 tbsp = 3 tsp)
    const totalRubTsp = tbspToTsp(totalRubTbsp);

    // Calculate quarter teaspoons (1 tsp = 4 quarter tsp)
    const totalQuarterTsp = totalRubTsp * 4;

    // Calculate total sodium from rub
    const totalRubSodium = totalQuarterTsp * rubSodiumPerQuarterTsp;

    return {
        numberOfRacks: numberOfRacks.toFixed(1),
        totalRubTbsp: totalRubTbsp.toFixed(1),
        totalRubTsp: totalRubTsp.toFixed(1),
        totalQuarterTsp: totalQuarterTsp.toFixed(1),
        totalRubSodium: totalRubSodium.toFixed(1)
    };
}

// Calculate additional salt needed
function calculateAdditionalSalt(ribWeight, rubSodiumPerQuarterTsp) {
    // Recommended total sodium for the weight
    const recommendedTotalSodium = ribWeight * RECOMMENDED_SODIUM_PER_LB;

    // Sodium from rub
    const rubCalculation = calculateRubSodium(rubSodiumPerQuarterTsp, ribWeight);
    const sodiumFromRub = parseFloat(rubCalculation.totalRubSodium);

    // Additional sodium needed
    const additionalSodiumNeeded = recommendedTotalSodium - sodiumFromRub;

    // Convert to salt amount (teaspoons of kosher salt)
    const additionalSaltTsp = additionalSodiumNeeded / KOSHER_SALT_MG_PER_TSP;

    return {
        recommendedTotalSodium: recommendedTotalSodium.toFixed(1),
        sodiumFromRub: sodiumFromRub,
        additionalSodiumNeeded: Math.max(0, additionalSodiumNeeded).toFixed(1),
        additionalSaltTsp: Math.max(0, additionalSaltTsp).toFixed(2),
        rubCalculation: rubCalculation
    };
}

// Routes
app.get('/', (req, res) => {
    res.render('index', {
        calculation: null,
        inputs: {
            ribWeight: '',
            rubSodium: ''
        }
    });
});

app.post('/calculate', (req, res) => {
    const { ribWeight, rubSodium } = req.body;

    const ribWeightNum = parseFloat(ribWeight);
    const rubSodiumNum = parseFloat(rubSodium);

    if (isNaN(ribWeightNum) || isNaN(rubSodiumNum) || ribWeightNum <= 0 || rubSodiumNum < 0) {
        return res.render('index', {
            calculation: null,
            inputs: { ribWeight, rubSodium },
            error: 'Please enter valid numbers. Rib weight must be greater than 0.'
        });
    }

    const calculation = calculateAdditionalSalt(ribWeightNum, rubSodiumNum);

    res.render('index', {
        calculation: calculation,
        inputs: { ribWeight, rubSodium },
        error: null
    });
});

app.listen(PORT, () => {
    console.log(`BBQ Salt Calculator running on http://localhost:${PORT}`);
});
