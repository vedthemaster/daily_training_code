"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.reducer = exports.actionCreators = void 0;
// ----------------
// ACTION CREATORS - These are functions exposed to UI components that will trigger a state transition.
// They don't directly mutate state, but they can have external side-effects (such as loading data).
exports.actionCreators = {
    requestSections: function (sectionIdIndex) { return function (dispatch, getState) {
        // Only load data if it's something we don't already have (and are not already loading)
        var appState = getState();
        if (appState && appState.sections && sectionIdIndex !== appState.sections.sectionIdIndex) {
            fetch("api/sectionsapi")
                .then(function (response) { return response.json(); })
                .then(function (data) {
                dispatch({ type: 'RECEIVE_DEPARTMENTS', sectionIdIndex: sectionIdIndex, sections: data });
            });
            dispatch({ type: 'REQUEST_DEPARTMENTS', sectionIdIndex: sectionIdIndex });
        }
    }; }
};
// ----------------
// REDUCER - For a given state and action, returns the new state. To support time travel, this must not mutate the old state.
var unloadedState = { sections: [], isLoading: false };
var reducer = function (state, incomingAction) {
    if (state === undefined) {
        return unloadedState;
    }
    var action = incomingAction;
    switch (action.type) {
        case 'REQUEST_DEPARTMENTS':
            return {
                sectionIdIndex: action.sectionIdIndex,
                sections: state.sections,
                isLoading: true
            };
        case 'RECEIVE_DEPARTMENTS':
            // Only accept the incoming data if it matches the most recent request. This ensures we correctly
            // handle out-of-order responses.
            if (action.sectionIdIndex === state.sectionIdIndex) {
                return {
                    sectionIdIndex: action.sectionIdIndex,
                    sections: action.sections,
                    isLoading: false
                };
            }
            break;
    }
    return state;
};
exports.reducer = reducer;
//# sourceMappingURL=Sections.js.map