function chart() {
    /* ChartJS
     * -------
     * Here we will create a few charts using ChartJS
     */

    //--------------
    //- AREA CHART -
    //--------------

    // Get context with jQuery - using jQuery's .get() method.
    var areaChartCanvas = $("#areaChart").get(0).getContext("2d");

    var areaChartData = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "Digital Goods",
                backgroundColor: "rgba(60,141,188,0.9)",
                borderColor: "rgba(60,141,188,0.8)",
                pointRadius: false,
                pointColor: "#3b8bba",
                pointStrokeColor: "rgba(60,141,188,1)",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(60,141,188,1)",
                data: [28, 48, 40, 19, 86, 27, 90],
            },
            {
                label: "Electronics",
                backgroundColor: "rgba(210, 214, 222, 1)",
                borderColor: "rgba(210, 214, 222, 1)",
                pointRadius: false,
                pointColor: "rgba(210, 214, 222, 1)",
                pointStrokeColor: "#c1c7d1",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [65, 59, 80, 81, 56, 55, 40],
            },
        ],
    };

    var areaChartOptions = {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false,
        },
        scales: {
            xAxes: [
                {
                    gridLines: {
                        display: false,
                    },
                },
            ],
            yAxes: [
                {
                    gridLines: {
                        display: false,
                    },
                },
            ],
        },
    };

    // This will get the first returned node in the jQuery collection.
    new Chart(areaChartCanvas, {
        type: "line",
        data: areaChartData,
        options: areaChartOptions,
    });

    //-------------
    //- LINE CHART -
    //--------------
    var lineChartCanvas = $("#lineChart").get(0).getContext("2d");
    var lineChartOptions = $.extend(true, {}, areaChartOptions);
    var lineChartData = $.extend(true, {}, areaChartData);
    lineChartData.datasets[0].fill = false;
    lineChartData.datasets[1].fill = false;
    lineChartOptions.datasetFill = false;

    var lineChart = new Chart(lineChartCanvas, {
        type: "line",
        data: lineChartData,
        options: lineChartOptions,
    });

    //-------------
    //- DONUT CHART -
    //-------------
    // Get context with jQuery - using jQuery's .get() method.
    var donutChartCanvas = $("#donutChart").get(0).getContext("2d");
    var donutData = {
        labels: ["Chrome", "IE", "FireFox", "Safari", "Opera", "Navigator"],
        datasets: [
            {
                data: [700, 500, 400, 600, 300, 100],
                backgroundColor: [
                    "#f56954",
                    "#00a65a",
                    "#f39c12",
                    "#00c0ef",
                    "#3c8dbc",
                    "#d2d6de",
                ],
            },
        ],
    };
    var donutOptions = {
        maintainAspectRatio: false,
        responsive: true,
    };
    //Create pie or doughnut chart
    // You can switch between pie and doughnut using the method below.
    new Chart(donutChartCanvas, {
        type: "doughnut",
        data: donutData,
        options: donutOptions,
    });

    //-------------
    //- PIE CHART -
    //-------------
    // Get context with jQuery - using jQuery's .get() method.
    var pieChartCanvas = $("#pieChart").get(0).getContext("2d");
    var pieData = donutData;
    var pieOptions = {
        maintainAspectRatio: false,
        responsive: true,
    };
    //Create pie or doughnut chart
    // You can switch between pie and doughnut using the method below.
    new Chart(pieChartCanvas, {
        type: "pie",
        data: pieData,
        options: pieOptions,
    });

    //-------------
    //- BAR CHART -
    //-------------
    var barChartCanvas = $("#barChart").get(0).getContext("2d");
    var barChartData = $.extend(true, {}, areaChartData);
    var temp0 = areaChartData.datasets[0];
    var temp1 = areaChartData.datasets[1];
    barChartData.datasets[0] = temp1;
    barChartData.datasets[1] = temp0;

    var barChartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        datasetFill: false,
    };

    new Chart(barChartCanvas, {
        type: "bar",
        data: barChartData,
        options: barChartOptions,
    });

    //---------------------
    //- STACKED BAR CHART -
    //---------------------
    var stackedBarChartCanvas = $("#stackedBarChart").get(0).getContext("2d");
    var stackedBarChartData = $.extend(true, {}, barChartData);

    var stackedBarChartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [
                {
                    stacked: true,
                },
            ],
            yAxes: [
                {
                    stacked: true,
                },
            ],
        },
    };

    new Chart(stackedBarChartCanvas, {
        type: "bar",
        data: stackedBarChartData,
        options: stackedBarChartOptions,
    });
}

//data visualization chart 
function charts() {
  const chart = document.getElementById("myChart").getContext("2d");
    
  //counting id and amount from budget url
  $(document).ready(function () {
    $.ajax({
      type: "GET",
        url: "/budgetAccounts",
      dataType: "json",
        success: function (data) {
          //JSON.parse(data);
          //console.log("Success : " + JSON.stringify(data));
            var context1 = data.data1;
            var context2 = data.data2;

          //get days to set its text budget frequency
          var Monday = $("#monday");
          var Tuesday = $("#tuesday");
          var Wednesday = $("#wednesday");
          var Thursday = $("#thursday");
          var Friday = $("#friday");
          var Saturday = $("#saturday");
          var Sunday = $("#sunday");

          //get days to set its text budget amounts
            var monday_amount = $("#monday_amount");
            var tuesday_amount = $("#tuesday_amount");
            var wednesday_amount = $("#wednesday_amount");
            var thursday_amount = $("#thursday_amount");
            var friday_amount = $("#friday_amount");
            var saturday_amount = $("#saturday_amount");
            var sunday_amount = $("#sunday_amount");
            var weekly= $("#weekly");
            var weekly_amount = $("#weekly_amount");


            //set the values for budget frequency and amount
            Monday.html(context1[0]);
            monday_amount.html(context1[7]).prepend('Tsh: ');
            Tuesday.html(context1[1]);
            tuesday_amount.html(context1[8]).prepend("Tsh: ");
            Wednesday.html(context1[2]);
            wednesday_amount.html(context1[9]).prepend("Tsh: ");
            Thursday.html(context1[3]);
            thursday_amount.html(context1[10]).prepend("Tsh: ");
            Friday.html(context1[4]);
            friday_amount.html(context1[11]).prepend("Tsh: ");
            Saturday.html(context1[5]);
            saturday_amount.html(context1[12]).prepend("Tsh: ");
            Sunday.html(context1[6]);
            sunday_amount.html(context1[13]).prepend("Tsh: ");
            weekly.html(context2).prepend("you budgeted for ");
            weekly.append('  times per week');
            
            var weekTotal = context1[7] + context1[8] + context1[9] + context1[10] + context1[11] + context1[12] + context1[13];
            //Math.format(weekTotal);
            const options = { 
                style: "currency",
                currencyFormat: "USD",
                minimumFractionDigits: 2,
                maximumFractionDigits:2
            }
            
            //weekTotal.toLocaleString('en-US');
            //var formatWeeklyTotal = weekTotal.toLocaleString('en-US', options);
            weekly_amount.html(weekTotal).prepend('Tsh: ');


        },
      error: function (xhr, textStatus, errorThrown) {
        console.log(textStatus);
        console.log("error: " + errorThrown);
      },
    });
  }),
    //ajax 2 functions for  loading data from expense url
    $.ajax({
      type: "GET",
        url: "/expenseAccounts",
      dataType: "json",
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
      success: function (data) {
        //JSON.parse(data);
          $.ajax({
            type: "GET",
            url: "/budgetAccounts",
            dataType: "json",
              csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
              success: function (data1) {
                var expense = data.ex_data;
                var expenseTotal = data.ex_data3;
                var budget = data1.data1;
                var budgetTotal = data1.data2;
                var day_budget = data.budget_day;

                //get days to set its text expense frequency
                var Monday = $("#monday_ex");
                var Tuesday = $("#tuesday_ex");
                var Wednesday = $("#wednesday_ex");
                var Thursday = $("#thursday_ex");
                var Friday = $("#friday_ex");
                var Saturday = $("#saturday_ex");
                var Sunday = $("#sunday_ex");

                //get days to set its text expense amounts
                var monday_amount = $("#monday_amount_expense");
                var tuesday_amount = $("#tuesday_amount_expense");
                var wednesday_amount = $("#wednesday_amount_expense");
                var thursday_amount = $("#thursday_amount_expense");
                var friday_amount = $("#friday_amount_expense");
                var saturday_amount = $("#saturday_amount_expense");
                var sunday_amount = $("#sunday_amount_expense");
                var weeklyExpense = $("#weeklyExpense");
                var weekly_amount = $("#weekly_amount_expense");

                //set the values for expense frequency and amount
                Monday.html(expense[0]);
                monday_amount.html(expense[7]).prepend("Tsh: ");
                Tuesday.html(expense[1]);
                tuesday_amount.html(expense[8]).prepend("Tsh: ");
                Wednesday.html(expense[2]);
                wednesday_amount.html(expense[9]).prepend("Tsh: ");
                Thursday.html(expense[3]);
                thursday_amount.html(expense[10]).prepend("Tsh: ");
                Friday.html(expense[4]);
                friday_amount.html(expense[11]).prepend("Tsh: ");
                Saturday.html(expense[5]);
                saturday_amount.html(expense[12]).prepend("Tsh: ");
                Sunday.html(expense[6]);
                sunday_amount.html(expense[13]).prepend("Tsh: ");
                weeklyExpense.html(expenseTotal).prepend("you expended for ");
                weeklyExpense.append("  times per week");

                var weekTotal =
                  expense[7] +
                  expense[8] +
                  expense[9] +
                  expense[10] +
                  expense[11] +
                  expense[12] +
                  expense[13];
               weekly_amount.html(weekTotal).prepend("Tsh: ");

                var status = [
                  "complete",
                  "success",
                  "failed",
                  "aborted",
                  "committed",
                  "pending",
                ];
                weeklyTotalExpenses =
                  expense[7] +
                  expense[8] +
                  expense[9] +
                  expense[10] +
                  expense[11] +
                  expense[12] +
                  expense[13];
                weeklyTotalBudget =
                  budget[7] +
                  budget[8] +
                  budget[9] +
                  budget[10] +
                  budget[11] +
                  budget[12] +
                  budget[13];
                var statusSet = $(".status");

                //get budget amount for each day
                var monday_budget_amount = budget[7];
                var tuesday_budget_amount = budget[8];
                var wednesday_budget_amount = budget[9];
                var thursday_budget_amount = budget[10];
                var friday_budget_amount = budget[11];
                var saturday_budget_amount = budget[12];
                var sunday_budget_amount = budget[13];

               //get expense for each day
                var monday_expense_amount = expense[7];
                var tuesday_expense_amount = expense[8];
                var wednesday_expense_amount = expense[9];
                var thursday_expense_amount = expense[10];
                var friday_expense_amount = expense[11];
                var saturday_expense_amount = expense[12];
                var sunday_expense_amount = expense[13];

                //now set status according to the budget settings
                var day = $("#day_budget").val();
                
                //create chart for budget
                let chartBrowser = new Chart(chart, {
                  type: "bar",
                  data: {
                    labels: [
                      "monday",
                      "Tuesday",
                      "Wednesday",
                      "Thursday",
                      "Friday",
                      "Saturday",
                      "Sunday",
                    ],
                    datasets: [
                      {
                        label: "Weekly Budget",
                        data: [
                          monday_budget_amount,
                          tuesday_budget_amount,
                          wednesday_budget_amount,
                          thursday_budget_amount,
                          friday_budget_amount,
                          saturday_budget_amount,
                          sunday_budget_amount,
                        ],
                        backgroundColor: [
                          "#f56954",
                          "#00a65a",
                          "#f39c12",
                          "#00c0ef",
                          "#3c8dbc",
                          "#d2d6de",
                        ],
                        barThickness: 50,
                      },
                    ],
                    options: {},
                  },
                });
              }//ajax charts ends here 
          });
        },
        error: function (xhr, textStatus, errorThrown) {
         //alert(errorThrown);
         }
    })
}
//show password
$(document).ready(function () {
  var monday_bar = $("#monday_amount");
  var passwordField = $("#password");
  var checkbox = $("#show");

  checkbox.on("click", function (e) {
   
    if (!checkbox.checked) {
      e.preventDefault();
    }
    else if (passwordField.type === "password") {
      passwordField.type = "text";
    }
    else {
      passwordField.type = "password";
    }
  })
})

//jquery code blocks for searching using ajax requests
$(document).ready(function () {
    var item = $('#day_category').val();
    $('#search').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'GET',
            url: ['/budgetList/', '/expenseList/'],
            data: { 'data': item },
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          success: function (data) {
            $.ajx({
              type: 'GET',
              url: '/salesList',
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
              success: function (sales_data) { 
              
              }
              })
      
            },
            error: function (status, error) {
                $('#response').html(status, ': ' + error);
            }
        })
    })
 
    //hide and show tables
    $('#budget').on('click', function (e) {
        $('#tb1').show();
        $('#tb2').hide();
      $('#th2').remove();
      $('#tbl2').empty();
      //hide sales list
      $("#table_sales").hide();
      $("#table_sales").empty();
      $('#tbl3').empty();
      $('#tbl3').hide();
      $('#tb3').hide();
      $('#th3').hide();

    }),
        $('#expense').on('click', function (e) {
            $('#tb2').show();
            $('#tb1').hide();
          $('#th1').remove();
          $('#tbl1').empty();
          //hide sale list
          $("#table_sales").hide();
          $("#table_sales").empty();
          $("#tbl3").empty();
          $("#tbl3").hide();
          $('#tb3').hide();
          $("#th3").hide();
        }),
      $('#sales').on('click', function (e) {
        //show sales
        $("#table_sales").show();
        $('#tb3').show();
         $("#tbl3").show();
         $("#th3").show();
       // hide budget table
        $("#tb1").hide();
        $("#tb2").hide();
        $("#th2").remove();
        $("#tbl2").empty();
       //hide expense table
         $("#tb2").hide();
         $("#tb1").hide();
         $("#th1").remove();
         $("#tbl1").empty();
        
      })
});    
 //execute count function 
document.addEventListener('DOMContentLoaded', function () { 
    
})

function loadImages() { 
    document.addEventListener("DOMContentLoaded", function () {
      $(document).ready(function () {
        $.ajax({
          type: "GET",
          url: "/CarouselSlide",
          csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
          success: function (data) {
            //console.log(data.slides.url);
          },
          error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus + "   " + errorThrown);
          },
        });
      });
    });
}
//dismiss alert buttons
$(document).ready(function () {
  $(".close").click(function (e) {
    e.preventDefault();
        
    $('.alert').hide();
  })
});



//prepare the report for the week
function report() {
  $(document).ready(function () {
    
      $.ajax({
        type: 'GET',
        url: '/getSalesReport',
        dataType: 'json',
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        success: function (sales_data) {
          $.ajax({
            type: 'GET',
            url: '/getBudgetReport',
            dataType: 'json',
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            success: function (budget_data) {
              $.ajax({
                type: 'GET',
                url: '/getExpenseReport',
                dataType: 'json',
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                success: function (expense_data) {
                  //write code logic here
                  sales = sales_data.sales_report;
                  budgets = budget_data.data1;
                  expense = expense_data.ex_data;
                  
                  //get days to set its text sales amounts
                  var monday_amount = $("#monday_sales_summary");
                  var tuesday_amount = $("#tuesday_sales_summary");
                  var wednesday_amount = $("#wednesday_sales_summary");
                  var thursday_amount = $("#thursday_sales_summary");
                  var friday_amount = $("#friday_sales_summary");
                  var saturday_amount = $("#saturday_sales_summary");
                  var sunday_amount = $("#sunday_sales_summary");
                  var weekly_amount = $("#weekly_sales_summary");

                  //set table data its html contents
                  monday_amount.html(sales[7]).prepend("Tsh: ");
                  tuesday_amount.html(sales[8]).prepend("Tsh: ");
                  wednesday_amount.html(sales[9]).prepend("Tsh: ");
                  thursday_amount.html(sales[10]).prepend("Tsh: ");
                  friday_amount.html(sales[11]).prepend("Tsh: ");
                  saturday_amount.html(sales[12]).prepend("Tsh: ");
                  sunday_amount.html(sales[13]).prepend("Tsh: ");
                  weekly_amount.html(sales[14]).prepend("Tsh: ");

                  //get days to set its text budget amounts
                  var monday_budget_amount = $("#monday_budget_summary");
                  var tuesday_budget_amount = $("#tuesday_budget_summary");
                  var wednesday_budget_amount = $("#wednesday_budget_summary");
                  var thursday_budget_amount = $("#thursday_budget_summary");
                  var friday_budget_amount = $("#friday_budget_summary");
                  var saturday_budget_amount = $("#saturday_budget_summary");
                  var sunday_budget_amount = $("#sunday_budget_summary");
                  var weekly_budget_amount = $("#weekly_budget_summary");

                  //set the table contents for BudgetAmount
                  monday_budget_amount.html(budgets[7]).prepend("Tsh: ");
                  tuesday_budget_amount.html(budgets[8]).prepend("Tsh: ");
                  wednesday_budget_amount.html(budgets[9]).prepend("Tsh: ");
                  thursday_budget_amount.html(budgets[10]).prepend("Tsh: ");
                  friday_budget_amount.html(budgets[11]).prepend("Tsh: ");
                  saturday_budget_amount.html(budgets[12]).prepend("Tsh: ");
                  sunday_budget_amount.html(budgets[13]).prepend("Tsh: ");
                  weekly_budget_amount.html(budgets[14]).prepend("Tsh: ");

                  //get days to set its text expense amounts
                  var monday_expense_amount = $("#monday_expense_summary");
                  var tuesday_expense_amount = $("#tuesday_expense_summary");
                  var wednesday_expense_amount = $("#wednesday_expense_summary");
                  var thursday_expense_amount = $("#thursday_expense_summary");
                  var friday_expense_amount = $("#friday_expense_summary");
                  var saturday_expense_amount = $("#saturday_expense_summary");
                  var sunday_expense_amount = $("#sunday_expense_summary");
                  var weekly_expense_amount = $("#weekly_expense_summary");

                  //set the table contents for the summary expanse amounts
                  monday_expense_amount.html(expense[7]).prepend('Tsh: ');
                  tuesday_expense_amount.html(expense[8]).prepend('Tsh: ');
                  wednesday_expense_amount.html(expense[9]).prepend('Tsh: ');
                  thursday_expense_amount.html(expense[10]).prepend('Tsh: ');
                  friday_expense_amount.html(expense[11]).prepend('Tsh: ');
                  saturday_expense_amount.html(expense[12]).prepend('Tsh: ');
                  sunday_expense_amount.html(expense[13]).prepend('Tsh: ');
                  weekly_expense_amount.html(expense[14]).prepend('Tsh: ');


                },
                error: function (jqXHR, textStatus, errorThrown) {
                  console.log(errorThrown);
                }
              })
            }
          })
        }
      })
    })
}

function loadPage() {
  $.ajax({
    type: "GET",
    url: "/ReportPage",
    csrfmiddlewaretoken: $('input[name="csrfmiddleware').val(),
    success: function (data) { 

    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log(errorThrown);
    }
  });
}    
    
  
//set sales page
function salesPage() {
  const saleGraph = document.querySelector('#salesTrend').getContext('2d');
  $(document).ready(function () { 
    $.ajax({
      type: 'GET',
      url: '/salesAccounts',
      dataType: 'json',
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
      success: function (saleAccount) {
        
        var sales = saleAccount.sales;
        var salesTotal = saleAccount.sale;
        
        //get days to set its text sales frequency
        var Monday = $("#monday_sales");
        var Tuesday = $("#tuesday_sales");
        var Wednesday = $("#wednesday_sales");
        var Thursday = $("#thursday_sales");
        var Friday = $("#friday_sales");
        var Saturday = $("#saturday_sales");
        var Sunday = $("#sunday_sales");
        var weeklySales = $("#weekly_sales");

        //get days to set its text sales amounts
        var monday_amount = $("#monday_sales_amount");
        var tuesday_amount = $("#tuesday_sales_amount");
        var wednesday_amount = $("#wednesday_sales_amount");
        var thursday_amount = $("#thursday_sales_amount");
        var friday_amount = $("#friday_sales_amount");
        var saturday_amount = $("#saturday_sales_amount");
        var sunday_amount = $("#sunday_sales_amount");
        var weekly_amount = $("#weekly_sales_amount");

        //set sales quantity
        Monday.html(sales[0]);
        Tuesday.html(sales[1]);
        Wednesday.html(sales[2]);
        Thursday.html(sales[3]);
        Friday.html(sales[4]);
        Saturday.html(sales[5]);
        Sunday.html(sales[6]);

        //set sales amount
        monday_amount.html(sales[7]).prepend('Tsh: ');
        tuesday_amount.html(sales[8]).prepend('Tsh: ');
        wednesday_amount.html(sales[9]).prepend('Tsh: ');
        thursday_amount.html(sales[10]).prepend('Tsh: ');
        friday_amount.html(sales[11]).prepend('Tsh: '); 
        saturday_amount.html(sales[12]).prepend('Tsh: ');
        sunday_amount.html(sales[13]).prepend('Tsh: ');

        //set weekly sales price
        weeklySales.html(salesTotal).prepend('you sold for ').append(' times per week');
        TotalWeeklySales = sales[7] + sales[8] + sales[9] + sales[10] + sales[11] + sales[12] + sales[13];
        weekly_amount.html(TotalWeeklySales).prepend('Tsh: ');

        //set weekly graph daily amount
       var  monday_sales = sales[7];
       var tuesday_sales = sales[8];
       var wednesday_sales = sales[9];
       var thursday_sales = sales[10];
       var  friday_sales = sales[11];
       var  saturday_sales = sales[12];
       var  sunday_sales= sales[13];
      
        let salesChart = new Chart(saleGraph, {
          type: "bar",
          data: {
            labels: [
              "monday",
              "tuesday",
              "wednesday",
              "thursday",
              "friday",
              "saturday",
              "sunday",
            ],
            datasets: [
              {
                label: "Weekly Sales",
                data: [
                  monday_sales,
                  tuesday_sales,
                  wednesday_sales,
                  thursday_sales,
                  friday_sales,
                  saturday_sales,
                  sunday_sales,
                ],
                backgroundColor: [
                  "teal",
                  "#f56954",
                  "#00a65a",
                  "#f39c12",
                  "#00c0ef",
                  "#3c8dbc",
                  "#d2d6de",
                ],
                barThickness: 50,
              },
            ],
            options: {},
          },
        });

        
      }
    })
  });
}


//print report
function hideButton() {
  $(document).ready(function () {
    $('#print').on('click', function () { 
      $(this).hide();
      $(this).remove();
    })
  })
}

function toggleNavBar() {
  $(function () {
    var nav = $("#sidebarMenu");
    nav.hide();
    var buttonToggle = $("<button class='navbar-toggler position-absolute d-md-none collapsed' type='button' data-bs-toggle='collapse' id='toggleButton' data-bs-target='#sidebarMenu' aria-controls='sidebarMenu' aria-expanded='false' aria-label='Toggle navigation'>");
    var logo = $("#logo");
    logo
      .append(buttonToggle)
      .append("<span class='navbar-toggler-icon'></span>");
    buttonToggle.on("click", function () {
      nav.hide();
    });
  });
}

function expense() {
  const expenseChart = document.getElementById('expenseChart').getContext('2d');
  $(document).ready(function () { 
    $.ajax({
      type: "GET",
      url: "/expenseAccounts",
      dataType: "json",
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
      success: function (data) {
        var expense = data.ex_data;
        var expenseTotal = data.ex_data3;

        //get days to set its text expense frequency
        var Monday = $("#monday_ex");
        var Tuesday = $("#tuesday_ex");
        var Wednesday = $("#wednesday_ex");
        var Thursday = $("#thursday_ex");
        var Friday = $("#friday_ex");
        var Saturday = $("#saturday_ex");
        var Sunday = $("#sunday_ex");

        //get days to set its text expense amounts
        var monday_amount = $("#monday_amount_expense");
        var tuesday_amount = $("#tuesday_amount_expense");
        var wednesday_amount = $("#wednesday_amount_expense");
        var thursday_amount = $("#thursday_amount_expense");
        var friday_amount = $("#friday_amount_expense");
        var saturday_amount = $("#saturday_amount_expense");
        var sunday_amount = $("#sunday_amount_expense");
        var weeklyExpense = $("#weeklyExpense");
        var weekly_amount = $("#weekly_amount_expense");

        //set the values for expense frequency and amount
        Monday.html(expense[0]);
        monday_amount.html(expense[7]).prepend("Tsh: ");
        Tuesday.html(expense[1]);
        tuesday_amount.html(expense[8]).prepend("Tsh: ");
        Wednesday.html(expense[2]);
        wednesday_amount.html(expense[9]).prepend("Tsh: ");
        Thursday.html(expense[3]);
        thursday_amount.html(expense[10]).prepend("Tsh: ");
        Friday.html(expense[4]);
        friday_amount.html(expense[11]).prepend("Tsh: ");
        Saturday.html(expense[5]);
        saturday_amount.html(expense[12]).prepend("Tsh: ");
        Sunday.html(expense[6]);
        sunday_amount.html(expense[13]).prepend("Tsh: ");
        weeklyExpense.html(expenseTotal).prepend("you expended for ");
        weeklyExpense.append("  times per week");

        var weekTotal =
          expense[7] +
          expense[8] +
          expense[9] +
          expense[10] +
          expense[11] +
          expense[12] +
          expense[13];
        weekly_amount.html(weekTotal).prepend("Tsh: ");

        var status = [
          "complete",
          "success",
          "failed",
          "aborted",
          "committed",
          "pending",
        ];
        weeklyTotalExpenses =
          expense[7] +
          expense[8] +
          expense[9] +
          expense[10] +
          expense[11] +
          expense[12] +
          expense[13];
        weeklyTotalBudget =
          budget[7] +
          budget[8] +
          budget[9] +
          budget[10] +
          budget[11] +
          budget[12] +
          budget[13];

        //get expense for each day
        var monday_expense_amount = expense[7];
        var tuesday_expense_amount = expense[8];
        var wednesday_expense_amount = expense[9];
        var thursday_expense_amount = expense[10];
        var friday_expense_amount = expense[11];
        var saturday_expense_amount = expense[12];
        var sunday_expense_amount = expense[13];
        
        //create chart
        let chartBrowser = new Chart(expenseChart, {
          type: "bar",
          data: {
            labels: [
              "monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday",
              "Sunday",
            ],
            datasets: [
              {
                label: "Weekly Budget",
                data: [
                  monday_expense_amount,
                  tuesday_expense_amount,
                  wednesday_expense_amount,
                  thursday_expense_amount,
                  friday_expense_amount,
                  saturday_expense_amount,
                  sunday_expense_amount,
                ],
                backgroundColor: [
                  "#00FFFF",
                  "#00a65a",
                  "#f39c12",
                  "#00c0ef",
                  "#3c8dbc",
                  "#d2d6de",
                  "#FFE4C4",
                ],
              },
            ],
            Options: {},
          },
        });
      },
      error: function (xhr, errorThrown, error) {
       console.log(error+ '  ' + errorThrown) 
      }
    });
  })
}

function setStatus() {
  $(document).ready(function () {
    var status = $('#status');
    $.ajax({
      type: "GET",
      url: "/saleStatus",
      dataType: "json",
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
      success: function (data) {
        var my_data = data.lists;
        for (i = 0; i < my_data.length; i++){
         // console.log(i[0]);
        }
      }
    });
   })
 }


//form submission for updating budget
function Budget() {
  $(document).ready(function () {
    var form = $("#myForm");
    form.on("submit", function () {
      var day = $('input[name="day"]').val();
      var date = $('input[name="date"]').val();
      var category = $('select[name="category"]').val();
      var quantity = $('input[name="quantity"]').val();
      var amount = $('input[name="amount"]').val();
      var description = $('textarea[name="description"]').val();

      $.ajax({
        type: "POST",
        url: "/update",
        data: {
          day: day,
          quantity: quantity,
          amount: amount,
          description: description,
          date: date,
          category: category,
        },
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        success: function (response) {
          window.log("data have been updated successfully");
          
        },
        error: function (status, error) {
          //window.confirm('data have not been updated yet');
          console.log(error + ", " + status);
        },
      });
    });
  });
}

function toggle() {
  var btn = document.getElementById("toggle");
  var nav = document.getElementById("sidebarMenu");
  console.log(nav);
  nav.style.display = "none";
}

function toggleView() {
  $(document).ready(function () {
    var nav = $("#sidebarMenu");
    var btn = $("#toggle");

    btn.on("click", function () {
      nav.hide();
    });
  });
}

//setting login user
function loginAuthenticate(){
  $(function(){
   var username =  localStorage.getItem("username");
   var item = $(".welcome");
   item.html(username).prepend("welcome ");
  })
}

//TO attach to an element this function use event="location=ordering();"
function ordering() {
  var url = new URL(window.location.href);
  var search_params = url.searchParams;
  search_params.set('order', document.querySelector("#sort").value);
  url.search = search_params.toString();
  var new_url = url.toString();
  return new_url;
}