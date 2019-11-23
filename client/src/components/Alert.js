  
import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

const Alert = ({ alerts }) => (
    alerts.map(alert => (
        <div key={alert.id} className={`alert alert-${alert.type} overlay-1`} role='alert'>
            {alert.msg}
        </div>
    ))
);

Alert.propTypes = {
    alerts: PropTypes.array.isRequired
}

const mapStateToProps = state => ({ 
    alerts: state.alerts
});

export default connect(
    mapStateToProps
)(Alert);