// Subcategory

import React from 'react';
import Typography from '@material-ui/core/Typography';

import './Subcategory.css';

export default function Subcategory(props) {
  let visible = true;

  const searchTermTrimmed = props.searchTerm.trim();
  
  if (searchTermTrimmed === '') {
    if (props.category === props.selectedCategory) {
      visible = true;
    } else {
      visible = false;
    }
  } else {
    visible = false;
  }

  if (visible) {
    return (
      <div className="subcategory">

        <div className="spacer">&nbsp;</div>

        <div className="subcategorytext">
          <Typography variant="body1">
            <b>{props.name.trim()}</b>
          </Typography>
        </div>

      </div>
    );
  } else {
    return null;
  }
}
