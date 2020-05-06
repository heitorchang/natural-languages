import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import Hidden from '@material-ui/core/Hidden';
import IconButton from '@material-ui/core/IconButton';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import MenuIcon from '@material-ui/icons/Menu';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

import E from './E';
import Subcategory from './Subcategory';
import PhrasesLabel from './PhrasesLabel';

import { processedData } from './data/processed';
import { categoryOrder } from './data/order';

import { makeStyles, useTheme } from '@material-ui/core/styles';

const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  drawer: {
    [theme.breakpoints.up('sm')]: {
      width: drawerWidth,
      flexShrink: 0,
    },
  },
  appBar: {
    backgroundColor: "#9BF",
    
    [theme.breakpoints.up('sm')]: {
      width: `calc(100% - ${drawerWidth}px)`,
      marginLeft: drawerWidth,
    },
  },
  menuButton: {
    marginRight: theme.spacing(2),
    [theme.breakpoints.up('sm')]: {
      display: 'none',
    },
  },
  // necessary for content to be below app bar
  toolbar: theme.mixins.toolbar,
  drawerPaper: {
    width: drawerWidth,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
}));

function ResponsiveDrawer(props) {
  const { window } = props;
  const classes = useStyles();
  const theme = useTheme();
  const [mobileOpen, setMobileOpen] = React.useState(false);
  const [searchTerm, setSearchTerm] = React.useState("");
  const [selectedCategory, setSelectedCategory] = React.useState("Need to know");

  const mainRef = React.useRef();
  const searchFieldRef = React.useRef();
  
  const menuItems = categoryOrder;
  
  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const loadCategory = (name) => {
    setSelectedCategory(name);
    if (mobileOpen) {
      setMobileOpen(false);
    }
    // clear search term
    setSearchTerm("");
    
    mainRef.current.scrollIntoView({ block: 'start' });
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
    mainRef.current.scrollIntoView({ block: 'start' });
  };

  const clearSearch = () => {
    setSearchTerm("");
    searchFieldRef.current.focus();
  };
  
  const drawer = (
    <div>
      <List>
        {menuItems.map((text, index) => (
          <ListItem button key={text} onClick={() => loadCategory(text)}>
            <ListItemText primary={text} />
          </ListItem>
        ))}
      </List>
    </div>
  );

  const container = window !== undefined ? () => window().document.body : undefined;

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            className={classes.menuButton}
          >
            <MenuIcon />
          </IconButton>

          <TextField value={searchTerm} size="medium" id="searchField" label="Search" variant="filled" onChange={handleSearchChange} inputRef={searchFieldRef} autoFocus />

          &nbsp;&nbsp;&nbsp;
          <Button variant="contained" color="primary" onClick={clearSearch}>
            Clear
          </Button>
          
        </Toolbar>
      </AppBar>
      
      <nav className={classes.drawer} aria-label="mailbox folders">
        {/* The implementation can be swapped with js to avoid SEO duplication of links. */}
        <Hidden smUp implementation="css">
          <Drawer
            container={container}
            variant="temporary"
            anchor={theme.direction === 'rtl' ? 'right' : 'left'}
            open={mobileOpen}
            onClose={handleDrawerToggle}
            classes={{
              paper: classes.drawerPaper,
            }}
            ModalProps={{
              keepMounted: true, // Better open performance on mobile.
            }}
          >
            {drawer}
          </Drawer>
        </Hidden>
        <Hidden xsDown implementation="css">
          <Drawer
            classes={{
              paper: classes.drawerPaper,
            }}
            variant="permanent"
            open
          >
            {drawer}
          </Drawer>
        </Hidden>
      </nav>
      <main className={classes.content} ref={mainRef}>
        <div className={classes.toolbar} />
        <Typography variant="h6">
          <PhrasesLabel selectedCategory={selectedCategory} searchTerm={searchTerm} />
        </Typography>

        { processedData.map(row => {
          return row[1][0] === "*" ?
            <Subcategory category={row[0]} name={row[1].toUpperCase().replace("*", "")} searchTerm={searchTerm} selectedCategory={selectedCategory} /> :
          <E category={row[0]} eng={row[1]} ita={row[2]} searchTerm={searchTerm} selectedCategory={selectedCategory} />;
        })}

        <br />
        <br />
        <br />
        <br />
        <br />
      </main>
    </div>
  );
}

export default ResponsiveDrawer;
