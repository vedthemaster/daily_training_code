import { Action, Reducer } from 'redux';
import { AppThunkAction } from '.';

// -----------------
// STATE - This defines the type of data maintained in the Redux store.

export interface SectionsState {
    isLoading: boolean;
    sectionIdIndex?: number;
    sections: Section[];
}

export interface Section {
    sectionId: number;
    sectionName: string;
}

// -----------------
// ACTIONS - These are serializable (hence replayable) descriptions of state transitions.
// They do not themselves have any side-effects; they just describe something that is going to happen.

interface RequestSectionsAction {
    type: 'REQUEST_DEPARTMENTS';
    sectionIdIndex: number;
}

interface ReceiveSectionsAction {
    type: 'RECEIVE_DEPARTMENTS';
    sectionIdIndex: number;
    sections: Section[];
}

// Declare a 'discriminated union' type. This guarantees that all references to 'type' properties contain one of the
// declared type strings (and not any other arbitrary string).
type KnownAction = RequestSectionsAction | ReceiveSectionsAction;

// ----------------
// ACTION CREATORS - These are functions exposed to UI components that will trigger a state transition.
// They don't directly mutate state, but they can have external side-effects (such as loading data).

export const actionCreators = {
    requestSections: (sectionIdIndex: number): AppThunkAction<KnownAction> => (dispatch, getState) => {
        // Only load data if it's something we don't already have (and are not already loading)
        const appState = getState();
        if (appState && appState.sections && sectionIdIndex !== appState.sections.sectionIdIndex) {
            fetch(`api/sectionsapi`)
                .then(response => response.json() as Promise<Section[]>)
                .then(data => {
                    dispatch({ type: 'RECEIVE_DEPARTMENTS', sectionIdIndex: sectionIdIndex, sections: data });
                });

            dispatch({ type: 'REQUEST_DEPARTMENTS', sectionIdIndex: sectionIdIndex });
        }
    }
};

// ----------------
// REDUCER - For a given state and action, returns the new state. To support time travel, this must not mutate the old state.

const unloadedState: SectionsState = { sections: [], isLoading: false };

export const reducer: Reducer<SectionsState> = (state: SectionsState | undefined, incomingAction: Action): SectionsState => {
    if (state === undefined) {
        return unloadedState;
    }

    const action = incomingAction as KnownAction;
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