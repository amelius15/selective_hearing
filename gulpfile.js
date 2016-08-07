var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var sourcemaps = require('gulp-sourcemaps');
var babel = require('gulp-babel');
var browserify = require('browserify');
var babelify = require('babelify');
var vinylSource = require('vinyl-source-stream')
var vinylBuffer = require('vinyl-buffer')
var concat = require('gulp-concat')
var envify = require('loose-envify')
var eslint = require('gulp-eslint')
var merge = require('merge-stream')

var jsFiles = 'browser/**/*.js'
var cssFiles = 'browser/css/*.css'

gulp.task('lint', function () {
    return gulp.src(jsFiles)
    .pipe(eslint())
    .pipe(eslint.format())
})

gulp.task('js', ['lint'], function () {
    var prodString = 'development'
    console.log(`Compiling client-side javascript for ${prodString}`);

    var modulesOptions = {
        o:'public/css/app.css',
        after: 'autoprefixer'
    }

    return browserify('./browser/index.js', {debug: true})
        .transform(babelify)
        .transform(envify)
        .bundle()
        .on('error', function (err) {
            console.log(err.toString());
            this.emit("end");
        })
        .pipe(vinylSource('bundle.js'))
        .pipe(vinylBuffer())
        .pipe(sourcemaps.init({loadMaps: true}))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest('static/scripts'));
});

gulp.task('css', function() {
    var style = gulp.src('browser/css/*.css')
        .pipe(autoprefixer())
        .on('error', function (err) {
            console.log(err.toString());
            this.emit("end");
        })
        .pipe(gulp.dest('static/css'));

    return style
});

gulp.task('watch', function() {
    gulp.watch(cssFiles, ['css'])
    gulp.watch(jsFiles, ['js'])
})

gulp.task('compile', ['js', 'css'])
