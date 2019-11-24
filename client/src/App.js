import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux'
import store from './redux';
import Alert from './components/layout/Alert';
import Routes from './components/Routes';
import './App.css';

const App = () => {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <div className="app">
          <Alert />
          <Routes />
        </div>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
