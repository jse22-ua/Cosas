const EXPECTED_MINUTES_IN_OVEN = 40;

function remainingMinutesInOven(actual) {
    return EXPECTED_MINUTES_IN_OVEN - actual;
}

function preparationTimeInMinutes(numberOfLayers) {
    return numberOfLayers * 2;
}

function totalTimeInMinutes(numberOfLayers, actualMinutesInOven) {
    return actualMinutesInOven + preparationTimeInMinutes(numberOfLayers);
}

module.exports = {
    remainingMinutesInOven: remainingMinutesInOven,
    totalTimeInMinutes: totalTimeInMinutes,
    preparationTimeInMinutes: preparationTimeInMinutes
};


