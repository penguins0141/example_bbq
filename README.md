# BBQ Salt Calculator

A Node.js web application that helps calculate how much additional salt to add to BBQ ribs based on your rub's sodium content.

## Features

- **Variable Rib Weight**: Input any weight from 0.1 to 20 lbs
- **Variable Rub Sodium**: Adjustable from 100-300 mg per 1/4 tsp using a slider or direct input
- **Smart Calculations**: Automatically calculates:
  - Number of racks based on weight (2 lbs per rack average)
  - Amount of rub needed (4 tbsp per rack)
  - Sodium from rub based on your input
  - Additional salt needed to reach recommended sodium levels
- **Preset Examples**: Quick reference for popular rubs like Famous Dave's (110mg) and Joe's Big Meat Seasoning (210mg)

## Calculation Logic

- **Recommended Sodium**: 400 mg per lb for baby back ribs
- **Rub Usage**: 4 tablespoons per rack (average 2 lb rack)
- **Kosher Salt**: 480 mg sodium per teaspoon
- **Conversions**: 1 tbsp = 3 tsp, 1 tsp = 4 quarter-tsp

## Installation

1. Install Node.js dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Or start the production server:
```bash
npm start
```

4. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Enter the weight of your ribs in pounds
2. Set the sodium content of your rub per 1/4 teaspoon (use the slider or type directly)
3. Click "Calculate Salt Needed"
4. View the detailed results showing exactly how much additional kosher salt to add

## Example Calculations

### Famous Dave's Rib Rub (110mg per 1/4 tsp)
- 5 lbs of ribs = 2.5 racks
- Needs 10 tbsp of rub = 30 tsp = 120 quarter-tsp
- Sodium from rub: 120 × 110mg = 13,200mg
- Recommended total: 5 lbs × 400mg = 2,000mg
- **Result**: No additional salt needed (rub provides more than enough)

### Joe's Big Meat Seasoning (210mg per 1/4 tsp)
- 2 lbs of ribs = 1 rack
- Needs 4 tbsp of rub = 12 tsp = 48 quarter-tsp
- Sodium from rub: 48 × 210mg = 10,080mg
- Recommended total: 2 lbs × 400mg = 800mg
- **Result**: No additional salt needed

## Dependencies

- **Express**: Web framework
- **EJS**: Template engine for dynamic HTML
- **Nodemon**: Development server with auto-restart

## File Structure

```
bbq-salt-calculator/
├── server.js              # Main server file with calculation logic
├── package.json           # Dependencies and scripts
├── views/
│   └── index.ejs         # Main HTML template
└── public/
    └── styles.css        # CSS styling
```

## Contributing

Feel free to fork this project and submit pull requests for improvements!
