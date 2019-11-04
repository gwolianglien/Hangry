import axios from 'axios';
import React, { Fragment, useState, useEffect } from 'react';

const Contexts = () => {

  const [user, setContexts] = useState({'context': ''});
  // const [choices, setChoices] = useState({'list': []});  // for additional features
  const [contextsList, setContextsList] = useState([]);

  useEffect(() => {
    const loadContexts = async () => {
      try {
        const res = await axios.get('/api/interface/contexts');
        return res.data;
      } catch(err) {
        console.error(err.message);  // Temporary for handling error in dev
      }
    }
    loadContexts().then(res => {
      const contexts = res.split(';');
      setContextsList(contexts)
    });
  }, [contextsList.length]);

  const handleChange = event => {
    setContexts({
      ...user,
      [event.target.id]: event.target.value,
    });
    // dispatch({
    //   type: 'CONTEXTS',
    //   data: user.context,
    // })
  }

  // // For additional features later
  // const handleAdd = event => {
  //   if (!user.context) {
  //     alert('Please let us know what kind of place you want to visit!');
  //   }
  //   var curr = user.context;
  //   var index = choices.list.indexOf(curr);
  //   if (index !== -1) {
  //     alert('You already added this context!');
  //   }
  //   var temp = choices.list.push(curr);
  //   setChoices({'list': temp});
  // }

  return (
    <Fragment>
      <div className="form-group">
        <h5 htmlFor="context">What are you feeling for?</h5>
        <select className="form-control" id="context" onChange={event=>handleChange(event)} value={user.context}>
          {
            contextsList.map((context, i) => <option key={i} value={`${context}`}>{context}</option> )
          }
        </select>
      </div>
      {/* <div className="">
        {
          choices.list.map((context, j) => {
            return (
              <div class="card">
                <div class="card-header">
                  {context}
                </div>
              </div>
            )
          })
        }
      </div> */}
    </Fragment>


  )
}

export default Contexts;
