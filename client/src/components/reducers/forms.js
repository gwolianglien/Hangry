const initialState = {
  location: '',
  contexts: [],
  cuisines: [],
}

const forms = (state=initialState, action) => {
  switch(action.type) {
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

export default forms;
