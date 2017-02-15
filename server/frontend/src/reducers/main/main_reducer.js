import { MAIN_ACTION } from '../../action_types';

const INITIAL_STATE = {};

export default function(state = INITIAL_STATE, action) {
    switch(action.type) {
        case MAIN_ACTION:
            return action.payload;
        default:
            return state;
    }
}
