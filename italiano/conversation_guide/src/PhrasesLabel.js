import React from 'react';

export default function PhrasesLabel(props) {
  if (props.searchTerm.trim() === '') {
    return props.selectedCategory;
  } else {
    return "Search results";
  }
}
