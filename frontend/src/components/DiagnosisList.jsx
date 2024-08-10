import React from 'react';
import './DiagnosisList.css';

const capitalizeLabel = (label) => {
  return label.replace(/\b\w/g, char => char.toUpperCase());
};

const DiagnosisList = (props) => {

  return (
    <div className="diagnosisList">
      <h3>Top Diagnoses</h3>
      <div className="diagnoses">
        {props.diagnoses.map((diagnosis, index) => (
          <p key={index}>
            {capitalizeLabel(diagnosis.label)}: {diagnosis.percentage.toFixed(2)}%
          </p>
        ))}
      </div>
    </div>
  );
}

export default DiagnosisList;