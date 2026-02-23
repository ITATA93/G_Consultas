# questionnaire.QCLXXOQ

> Evaluación de Resultados y Evolución en Psicoterapia (OQ-45-2)

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación de Resultados y Evolución en Psicoterapia (OQ-45-2)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Registro |
| Q02 | time |  |  | SI | Hora de Registro |
| Q03 | varchar |  |  | SI | Sesión N° |
| Q04 | varchar |  |  | SI | 1.  Me llevo bien con otros |
| Q05 | varchar |  |  | SI | 2.  Me canso rápidamente |
| Q06 | varchar |  |  | SI | 3.  Nada me interesa |
| Q07 | varchar |  |  | SI | 4.  Me siento presionado (estresado) en el trabajo... |
| Q08 | varchar |  |  | SI | 5.  Me siento culpable |
| Q09 | varchar |  |  | SI | 6.  Me siento irritado, molesto |
| Q10 | varchar |  |  | SI | 7.  Me siento contento con mi matrimonio/pareja |
| Q11 | varchar |  |  | SI | 8.  Pienso en quitarme la vida |
| Q12 | varchar |  |  | SI | 9.  Me siento débil |
| Q13 | varchar |  |  | SI | 10. Me siento atemorizado |
| Q14 | varchar |  |  | SI | 11.Necesito tomar bebidas alcohólicas en la mañana... |
| Q15 | varchar |  |  | SI | 12. Encuentro satisfacción en mi trabajo/ escuela |
| Q16 | varchar |  |  | SI | 13. Soy una persona feliz |
| Q17 | varchar |  |  | SI | 14. Trabajo/estudio excesivamente (mas de la cuent... |
| Q18 | varchar |  |  | SI | 15. Me siento inútil |
| Q19 | varchar |  |  | SI | 16. Me abruman (angustian) los problemas de mi fam... |
| Q20 | varchar |  |  | SI | 17. Mi vida sexual me llena |
| Q21 | varchar |  |  | SI | 18. Me siento solo |
| Q22 | varchar |  |  | SI | 19. Discuto frecuentemente |
| Q23 | varchar |  |  | SI | 20. Me siento querido y que me necesitan |
| Q24 | varchar |  |  | SI | 21. Disfruto mi tiempo libre |
| Q25 | varchar |  |  | SI | 22. Tengo dificultades para concentrarme |
| Q26 | varchar |  |  | SI | 23. Me siento sin esperanza  en el futuro |
| Q27 | varchar |  |  | SI | 24. Estoy contento conmigo mismo |
| Q28 | varchar |  |  | SI | 25. Me perturban o molestan pensamientos de los qu... |
| Q29 | varchar |  |  | SI | 26. Me molesta que me critiquen porque tomo o me d... |
| Q30 | varchar |  |  | SI | 27. Tengo malestares estomacales |
| Q31 | varchar |  |  | SI | 28. Trabajo/estudio tan bien como lo hacía antes |
| Q32 | varchar |  |  | SI | 29. Mi corazón palpita demasiado |
| Q33 | varchar |  |  | SI | 30. Tengo dificultades para llevarme bien con mis ... |
| Q34 | varchar |  |  | SI | 31. Estoy satisfecho con mi vida |
| Q35 | varchar |  |  | SI | 32. Tengo problemas en el trabajo/escuela debido a... |
| Q36 | varchar |  |  | SI | 33. Siento que algo malo va a ocurrir |
| Q37 | varchar |  |  | SI | 34. Tengo los músculos adoloridos |
| Q38 | varchar |  |  | SI | 35. Me atemorizan los espacios abiertos, el maneja... |
| Q39 | varchar |  |  | SI | 36. Me siento nervioso |
| Q40 | varchar |  |  | SI | 37. Me satisfacen mis relaciones con mis seres que... |
| Q41 | varchar |  |  | SI | 38. Siento que  me va bien en el trabajo/escuela |
| Q42 | varchar |  |  | SI | 39. Tengo muchas discusiones en el trabajo/escuela |
| Q43 | varchar |  |  | SI | 40. Siento que algo anda mal con mi mente |
| Q44 | varchar |  |  | SI | 41. Tengo dificultades para dormir, o no me puedo ... |
| Q45 | varchar |  |  | SI | 42. Me siento triste |
| Q46 | varchar |  |  | SI | 43. Mis relaciones con otros me satisfacen |
| Q47 | varchar |  |  | SI | 44. Me enojo tanto en el trabajo/escuela que puedo... |
| Q48 | varchar |  |  | SI | 45. Me dan dolores de cabeza |
| Q49 | varchar |  |  | SI | SD |
| Q50 | varchar |  |  | SI | IR |
| Q51 | varchar |  |  | SI | SR |
| Q52 | varchar |  |  | SI | Sintomatología (SD): PC = 43 ICC = 12 |
| Q53 | varchar |  |  | SI | Un puntaje alto indica principalmente la presencia... |
| Q54 | varchar |  |  | SI | Un puntaje bajo indica la ausencia o la negación d... |
| Q55 | varchar |  |  | SI | Relaciones interpersonales (RI): PC = 16 ICC = 9 |
| Q56 | varchar |  |  | SI | Un puntaje alto indica dificultades en sus relacio... |
| Q57 | varchar |  |  | SI | Un puntaje bajo indica la ausencia de problemas in... |
| Q58 | varchar |  |  | SI | Rol social (RS): PC = 14 ICC = 8 |
| Q59 | varchar |  |  | SI | Un puntaje alto señala dificultades en el ajuste d... |
| Q60 | varchar |  |  | SI | Un puntaje bajo indica un adecuado ajuste al rol s... |
| Q61 | varchar |  |  | SI | donde el cliente podría contestar arbitrariamente ... |
| Q62 | varchar |  |  | SI | Puntaje Total: |
| Q63 | varchar |  |  | SI | Un puntaje alto indica que el cliente admite un el... |
| Q64 | varchar |  |  | SI | en tanto que un puntaje bajo sugiere que el client... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*