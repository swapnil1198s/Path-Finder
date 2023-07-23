import React from 'react';
import "./Maze.css"

const Maze = ({ maze }) => (
  <div className="maze">
    {maze.map((row, i) => (
      <div key={i} className="maze-row">
        {row.map((cell, j) => (
          <div key={j} className={`maze-cell maze-cell-${cell}`}></div>
        ))}
      </div>
    ))}
  </div>
);

export default Maze;
