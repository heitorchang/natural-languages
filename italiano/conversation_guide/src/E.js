// Dictionary Entry

import React from 'react';
import Typography from '@material-ui/core/Typography';

import './E.css';

export default function E(props) {
  let visible = true;

  const searchTermTrimmed = props.searchTerm.trim();
  
  if (searchTermTrimmed === '') {
    if (props.category === props.selectedCategory) {
      visible = true;
    } else {
      visible = false;
    }
  } else {
    const searchLower = searchTermTrimmed.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    const engLower = props.eng.toLowerCase();
    const itaLower = props.ita.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();

    const searchRegex = RegExp('\\b' + searchLower + '|^' + searchLower);
    
    if (searchRegex.test(engLower) || searchRegex.test(itaLower)) {
      visible = true;
    } else {
      visible = false;
    }
  }
  
  if (visible) {
    return (
      <div className="entry">

        <div className="spacer">&nbsp;</div>

        <div className="line eng">
          <Typography variant="body1">
            <b>{props.eng}</b>
          </Typography>
        </div>
        <div className="line ita">
          <Typography variant="body1">
            {props.ita}
          </Typography>
        </div>

      </div>
    );
  } else {
    return null;
  }
}
