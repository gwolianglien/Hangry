
export const addContext = context => async dispatch => {
  dispatch({
    type: 'ADD_CONTEXT',
    data: context
  });
}

export const removeContext = context => async dispatch => {
  dispatch({
    type: 'REMOVE_CONTEXT',
    data: context
  })
}
