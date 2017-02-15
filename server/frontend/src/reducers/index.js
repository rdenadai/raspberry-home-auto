import { combineReducers } from 'redux';
import MainReducer from './main/main_reducer';


const rootReducer = combineReducers({
    main: MainReducer
});

export default rootReducer;
