import React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Divider from '@material-ui/core/Divider';
import Drawer from '@material-ui/core/Drawer';
import Hidden from '@material-ui/core/Hidden';
import IconButton from '@material-ui/core/IconButton';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import MailIcon from '@material-ui/icons/Mail';
import MenuIcon from '@material-ui/icons/Menu';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';

import E from './E';
import PhrasesLabel from './PhrasesLabel';

import phrases from './phrases';

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
  const [selectedCategory, setSelectedCategory] = React.useState("Conversation");
  
  const menuItems = ['Conversation', 'Numbers', 'Time', 'Money', 'Getting around', 'Places to stay', 'Communications', 'Sightseeing', 'Shopping', 'Sports and leisure', 'Traveling with children', 'Emergencies', 'Police', 'Health', 'Pharmacy', 'Disabled travelers', 'Eating out', 'Meals and cooking', 'Drinks', 'On the menu', 'Going out', 'Romance'];
  
  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const loadCategory = (name) => {
    setSelectedCategory(name);
    if (mobileOpen) {
      setMobileOpen(false);
    }
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
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
          <Grid container justify="space-between">
            <Grid item>
              <TextField id="searchField" label="Search" variant="filled" onChange={handleSearchChange} />
            </Grid>

            <Grid item>
              <Typography variant="h6" noWrap>
                Italian Phrasebook
              </Typography>
            </Grid>
          </Grid>
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
      <main className={classes.content}>
        <div className={classes.toolbar} />
        <br />
        <Typography variant="h6">
          <PhrasesLabel selectedCategory={selectedCategory} searchTerm={searchTerm} />
        </Typography>

        <E category="Conversation" eng="Hello" ita="Ciao" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="Why?" ita="Perché" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="I'll call you" ita="La chiamo" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="Hello" ita="Ciao" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="Why?" ita="Perché" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="I'll call you" ita="La chiamo" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="Hello" ita="Ciao" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="Why?" ita="Perché" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="I'll call you" ita="La chiamo" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="Hello" ita="Ciao" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="Why?" ita="Perché" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Conversation" eng="I'll call you" ita="La chiamo" searchTerm={searchTerm} selectedCategory={selectedCategory} />

        <E category="Numbers" eng="one" ita="uno" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="Two" ita="Due" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="Three" ita="Tre" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="four" ita="Quattro" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="five" ita="Cinque" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="six" ita="Sei" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="Seven" ita="sette" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="Eight" ita="otto" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="nine" ita="nove" searchTerm={searchTerm} selectedCategory={selectedCategory} />
        <E category="Numbers" eng="ten" ita="Dieci" searchTerm={searchTerm} selectedCategory={selectedCategory} />
      </main>
    </div>
  );
}

export default ResponsiveDrawer;
