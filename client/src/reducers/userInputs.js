const initialState = {
  location: '',
  contexts: [],
  cuisines: [],
}

const userInputs = (state=initialState, action) => {
  switch(action.type) {
    case 'LOCATION':
      return {
        ...state,
        location: action.data
      }
    case 'CONTEXTS':
      return {
        ...state,
        contexts: action.data
      }
    case 'CUISINES':
      return {
        ...state,
        cuisines: action.data
      }
    case 'CLEAR':
      return {
        location: '',
        contexts: [],
        cuisines: [],
      }
    default:
      return state;
  }
}

export default userInputs;
