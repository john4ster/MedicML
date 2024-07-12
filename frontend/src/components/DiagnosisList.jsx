import React from 'react';
import './DiagnosisList.css';

const DiagnosisList = (props) => {

  return (
    <div className="diagnosisList">
      <h3>Top Diagnoses</h3>
      <div className="diagnoses">
        {props.diagnoses.map((diagnosis, index) => (
          <p key={index}>
            {diagnosis.name}: {diagnosis.percentage}%
          </p>
        ))}
      </div>
    </div>
  );
}

export default DiagnosisList;