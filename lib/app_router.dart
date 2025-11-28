import 'package:go_router/go_router.dart';
import 'pages/admissions_home_page.dart';



import 'pages/dose_page.dart';
import 'pages/average_grade_page.dart';
import 'pages/prioridadembarque.dart';

// import 'pages/tuition_page.dart';
// import 'pages/enrollment_fee_page.dart';
// import 'pages/credits_summary_page.dart';

final GoRouter appRouter = GoRouter(
  routes: [
    GoRoute(
      path: '/',
      builder: (_, __) => const AdmissionsHomePage(),
    ),
    GoRoute(
      path: '/tuition',
      builder: (_, __) => const DosePage(),
    ),
    
    GoRoute(
      path: '/fees',
      builder: (_, __) => const AverageGradePage(),
    ),
    GoRoute(
      path: '/credits',
      builder: (_, __) => const PrioridadEmbarquePage(),
    ),
    // GoRoute(
    //   path: '/credits_embarque',
    //   builder: (_, __) => const CreditsSummaryPage(),
    // ),

  ],
);
