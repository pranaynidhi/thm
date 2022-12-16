<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'phpmyadmin1' );

/** MySQL database username */
define( 'DB_USER', 'phpmyadmin' );

/** MySQL database password */
define( 'DB_PASSWORD', '12345' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         ':Nl5_18W@|(P)/6TZ^p-%PE5qb$v/GB/b e737GB<ubx*O}u8yGPE:eeFD#PT1RE' );
define( 'SECURE_AUTH_KEY',  '@[5K4Q%_gsP%x=QJ]#-lX`BXVNSu7o}5=ht}L~/t%Txt Gx+<BX=,MeiiCHcXvc^' );
define( 'LOGGED_IN_KEY',    ',;0^d77wq7mtnGM1o%WaN.MpMJ9Zj69sI^)2cIVdR3h>YP/S:~SrIn+0AY$Adz.K' );
define( 'NONCE_KEY',        '8)iFPNlnC3vyN1Gj4zd:0(Jp@!8{=heP/G[L/B*>j9SvjNVn,Ei?oqdp2@<:mb0l' );
define( 'AUTH_SALT',        'QSh/V/w-X~/P7!d),h7.Ax>>5/b3Go^^b*hB7:>>&]VIo 00iI>9k_^ Ent^F?- ' );
define( 'SECURE_AUTH_SALT', '>,V>-2!VKaBkkeRd|K&!([%}!;TfeA`@ikjcC/[]:: $.K&L.-`gk_3%t5/fu_Zd' );
define( 'LOGGED_IN_SALT',   'BOk(mP#GI:/ApR/z#w]p<-{smWKoG]qW=gAFR:W=tp_EVb:TN!@cVidma6l@2R$s' );
define( 'NONCE_SALT',       '<9l}/$WEnbVG<;%6#*/bqEZ]x%ZO/mA#.Gy{r-*q|cY,@0,m.rs4 [@]AN_:*/zh' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
