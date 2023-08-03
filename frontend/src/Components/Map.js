import React from 'react';
import "./Map.css"

const Map = ({ main_map, cellClick }) => {
  return (
    <div className="map">
      {main_map.map((row, i) => (
        <div key={i} className="map-row">
          {row.map((cell, j) => (
            <div key={j} onClick={()=>cellClick(i,j)} className={`map-cell map-cell-${cell}`}></div>
          ))}
        </div>
      ))}
    </div>)
};

export default Map;
