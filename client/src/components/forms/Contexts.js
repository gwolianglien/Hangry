import axios from 'axios';
import React, { useState, useEffect } from 'react';

const Contexts = () => {

  const [user, setContexts] = useState('context': '');
  const [choices, setChoices] = useState('list': []);
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

  const handleChange = event => setContexts({
    ...user,
    [event.target.id]: event.target.value,
  });

  const handleAdd = event => {
    if (!user.context) {
      alert('Please let us know what kind of place you want to visit!');
    }
    var curr = user.context;
    var index = choices.list.indexOf(curr);
    if (index !== -1) {
      alert('You already added this context!');
    }

    var temp = choices.list.push(curr);
    setChoices('list': temp);
  }

  const handleSubmit = async event => {
    event.preventDefault();
  }

  return (
    <form onSubmit={event=>handleSubmit(event)}>
      <div className="form-group">
        <label htmlFor="context">What are you feeling?</label>
        <select className="form-control" id="context" onChange={event=>handleChange(event)} value={user.context}>
          {
            contextsList.map((context, i) => <option key={i} value={`${context}`}>{context}</option> )
          }
        </select>
      </div>
    </form>
  )
}

export default Contexts;
