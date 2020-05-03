// Category

import React from 'react';

export default function Cat(props) {
  let visible = false;

  if (props.selectedCategory === props.name ||
      props.searchTerm !== '') {
    visible = true;
  }
    
  if (visible) {
    return (
      <div>
        My Category
      </div>
    );
  } else {
    return null;
  }
}
