
const initialState = {
  location: '',
  contexts: [],
  cuisines: [],
}

export default (currentState=initialState, action) => {
  switch(action.type) {
    case 'SET_LOCATION':
      return {
        ...currentState,
        location: action.data
      }
    case 'ADD_CONTEXT':
      var currentContextList = currentState.contexts;
      currentContextList.push(action.data);
      return {
        ...currentState,
        contexts: currentContextList
      }
    case 'REMOVE_CONTEXT':
      var currentContextList = currentState.contexts;
      var updatedContextList = currentContextList.map(context => context.toLowerCase().trim() !== action.data.toLowerCase().trim());
      return {
        ...currentState,
        contexts: updatedContextList
      }
    case 'ADD_CUISINE':
      var updatedCuisineList = currentState.cuisines;
      updatedCuisineList.push(action.data);
      return {
        ...currentState,
        contexts: updatedCuisineList
      }
    case 'REMOVE_CUISINE':
      var updatedCuisineList = currentState.cuisines;
      updatedCuisineList.map(cuisine => cuisine !== action.data);
      return {
        ...currentState,
        contexts: updatedCuisineList
      }
    case 'CLEAR':
      return {
        location: '',
        contexts: [],
        cuisines: [],
      }
    default:
      return currentState;
  }
}
