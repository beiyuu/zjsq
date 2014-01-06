module.exports = function(grunt) {
  grunt.initConfig({
    compass: {
      dev: {
        options: {
          cssDir: 'static/css/',
          sassDir: 'static/scss',
          environment: 'development'
        }
      },
      pub: {
        options: {
          cssDir: 'static/css/',
          sassDir: 'static/scss',
          environment: 'production'
        }
      }
    },

    watch: {
      css: {
        files: [
          'static/scss/*.scss',
          'static/scss/common/*.scss',
          'static/scss/page/*.scss'
        ],
        tasks: ['compass:dev']
      }
    },

    connect: {
      site1: {
        options: {
          port: 9001,
          hostname: '0.0.0.0'
          //Note that if this option is enabled, any tasks specified after this task will never run.
          //see there https://github.com/gruntjs/grunt-contrib-connect#keepalive
          //so use `grunt server:keepalive`
          //keepalive: true
        }
      }
    }
  })

  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-connect');

  grunt.registerTask('default', 'compass:pub');
  grunt.registerTask('server', ['connect', 'watch']);
}
