# SQLUser.MRC_PastHistConditCateg

**Schema:** SQLUser
**Columnas:** 211
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CATEG_ParRef | bigint | PK |  | NO | MRC_PastHistCondit Parent Reference |
| CATEG_Childsub | double |  |  | NO | Childsub |
| CATEG_Code | varchar |  |  | SI | Code |
| CATEG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CATEG_CreatedDate | date |  |  | SI | Created Date |
| CATEG_CreatedTime | time |  |  | SI | Created Time |
| CATEG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CATEG_DateFrom | date |  |  | SI | Date From |
| CATEG_DateTo | date |  |  | SI | Date To |
| CATEG_Desc | varchar |  |  | SI | Description |
| CATEG_RowId | varchar |  |  | NO | - |
| CATEG_UpdatedDate | date |  |  | SI | Updated Date |
| CATEG_UpdatedTime | time |  |  | SI | Updated Time |
| CATEG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QACTEV | - |  |  | SI | Esta evaluación corresponde a: |
| QAG | - |  |  | SI | Relación del Acompañante o Cuidador |
| QCSGP | - |  |  | SI | Semanas de Gestación al Nacer el Paciente |
| QDSA10M | - |  |  | SI | Desarrollo Alterado 10 Mes |
| QDSA12M | - |  |  | SI | Desarrollo Alterado 12 Mes |
| QDSA15M | - |  |  | SI | Desarrollo Alterado 15 Mes |
| QDSA18M | - |  |  | SI | Desarrollo Alterado 18 Mes |
| QDSA1M | - |  |  | SI | Desarrollo Alterado 1 Mes |
| QDSA21M | - |  |  | SI | Desarrollo Alterado 21 Mes |
| QDSA24M | - |  |  | SI | Desarrollo Alterado 24 Mes |
| QDSA2M | - |  |  | SI | Desarrollo Alterado 2 Mes |
| QDSA3M | - |  |  | SI | Desarrollo Alterado 3 Mes |
| QDSA4M | - |  |  | SI | Desarrollo Alterado 4 Mes |
| QDSA5M | - |  |  | SI | Desarrollo Alterado 5 Mes |
| QDSA6M | - |  |  | SI | Desarrollo Alterado 6 Mes |
| QDSA7M | - |  |  | SI | Desarrollo Alterado 7 Mes |
| QDSA8M | - |  |  | SI | Desarrollo Alterado 8 Mes |
| QDSA9M | - |  |  | SI | Desarrollo Alterado 9 Mes |
| QDSM1 | - |  |  | SI | (S) Fija la mirada en el rostro del animador |
| QDSM10 | - |  |  | SI | 9. (M) Intenta controlar la cabeza al ser llevado ... |
| QDSM11 | - |  |  | SI | 10. (L) Vocaliza dos sonidos diferentes |
| QDSM12 | - |  |  | SI | 11. (S) Sonríe en respuesta a la sonrisa de un exa... |
| QDSM13 | - |  |  | SI | 12. (CL) Busca con la vista la fuente del sonido |
| QDSM14 | - |  |  | SI | 13. (C) Sigue con la vista la argolla (ángulo de 1... |
| QDSM15 | - |  |  | SI | 14. (M) Mantiene la cabeza erguida al ser llevado ... |
| QDSM16 | - |  |  | SI | 15. (L) Vocalización prolongada |
| QDSM17 | - |  |  | SI | 16. (C) La cabeza sigue la cuchara que desaparece |
| QDSM18 | - |  |  | SI | 17. (C)(L) Gira la cabeza al sonido de la campanil... |
| QDSM19 | - |  |  | SI | 18. (M) En posición prona se levanta a sí mismo |
| QDSM20 | - |  |  | SI | 19. (M) Levanta la cabeza y hombros al ser llevado... |
| QDSM21 | - |  |  | SI | 20. (LS) Ríe a carcajada |
| QDSM22 | - |  |  | SI | 21. (S)(L) Vuelve la cabeza hacia quien le habla |
| QDSM23 | - |  |  | SI | 22. (C ) Palpa el borde de la mesa |
| QDSM24 | - |  |  | SI | 23. (C) Intenta prehensión de la argolla |
| QDSM25 | - |  |  | SI | 24. (M) Tracciona hasta lograr la posición sentada |
| QDSM26 | - |  |  | SI | 25. (M) Se Mantiene Sentado con leve apoyo |
| QDSM27 | - |  |  | SI | 26. (M) Se mantiene sentado solo, momentáneamente |
| QDSM28 | - |  |  | SI | 27. (C) Vuelve la cabeza hacia la cuchara caída |
| QDSM29 | - |  |  | SI | 28. (C) Coge la argolla |
| QDSM3 | - |  |  | SI | 2. (L) Reacciona al sonido de la campanilla |
| QDSM30 | - |  |  | SI | 29. (C) Coge el cubo |
| QDSM31 | - |  |  | SI | 30. (LS) Vocaliza cuando se le habla |
| QDSM32 | - |  |  | SI | 31. (M) Se mantiene sentado solo por 30 seg. o más |
| QDSM33 | - |  |  | SI | 32. (C) Intenta agarrar la pastilla |
| QDSM34 | - |  |  | SI | 33. (L) Escucha selectivamente palabras familiares |
| QDSM35 | - |  |  | SI | 34. (S) Coopera en los juegos |
| QDSM36 | - |  |  | SI | 35. (C) Coge dos cubos, uno en cada mano |
| QDSM37 | - |  |  | SI | 36. (M) Se sienta solo y se mantiene erguido |
| QDSM38 | - |  |  | SI | 37. (M) Tracciona hasta lograr la posición de pie |
| QDSM39 | - |  |  | SI | 38. (M) Iniciación de pasos sostenido bajo los bra... |
| QDSM4 | - |  |  | SI | 3. (M) Aprieta el dedo índice del examinador |
| QDSM40 | - |  |  | SI | 39. (C) Coge la pastilla con movimiento de rastril... |
| QDSM41 | - |  |  | SI | 40. (L) Dice da-da o equivalente |
| QDSM42 | - |  |  | SI | 41. (M) Logra llegar a posición de pie, apoyado en... |
| QDSM43 | - |  |  | SI | 42. (M) Camina sostenido bajo los brazos |
| QDSM44 | - |  |  | SI | 43. (C) Coge la pastilla con participación del pul... |
| QDSM45 | - |  |  | SI | 44. (C) Encuentra el cubo bajo el pañal |
| QDSM46 | - |  |  | SI | 45. (LS) Reacciona a los requerimientos verbales |
| QDSM47 | - |  |  | SI | 46. (C) Coge la pastilla con pulgar e índice |
| QDSM48 | - |  |  | SI | 47. (S) Imita gestos simples |
| QDSM49 | - |  |  | SI | 48. (C) Coge el tercer cubo dejando uno de los dos... |
| QDSM5 | - |  |  | SI | 4. (C) Sigue con la vista la argolla (ángulo de 90... |
| QDSM50 | - |  |  | SI | 49. (C) Combina cubos en la línea media |
| QDSM51 | - |  |  | SI | 50. (S)(L) Reacciona al no, no |
| QDSM52 | - |  |  | SI | 51. (M) Camina algunos pasos de la mano |
| QDSM53 | - |  |  | SI | 52. (C) Junta las manos en linea media |
| QDSM54 | - |  |  | SI | 53. (M) Se pone de pie solo |
| QDSM56 | - |  |  | SI | 55. (L) Dice al menos dos palabras |
| QDSM57 | - |  |  | SI | 56. (M) Camina solo |
| QDSM58 | - |  |  | SI | 57. (C) Introduce la pastilla en la botella |
| QDSM59 | - |  |  | SI | 58. (C) Espontáneamente garabatea |
| QDSM6 | - |  |  | SI | 5. (M) Movimiento de cabeza en posición prona |
| QDSM60 | - |  |  | SI | 59. (C) Coge el tercer cubo conservando los dos pr... |
| QDSM61 | - |  |  | SI | 60. (L) Dice al menos tres palabras |
| QDSM62 | - |  |  | SI | 61. (LS) Muestra sus zapatatos |
| QDSM63 | - |  |  | SI | 62. (M) Camina varios pasos hacia el lado |
| QDSM64 | - |  |  | SI | 63. (M) Camina varios pasos hacia el atrás |
| QDSM66 | - |  |  | SI | 65. (C) Atrae el cubo con un palo |
| QDSM67 | - |  |  | SI | 66. (L) Nombra un objeto de los cuatro presentados |
| QDSM68 | - |  |  | SI | 67. (L) Imita tres palabras en el momento del exam... |
| QDSM69 | - |  |  | SI | 68. (C) Construye una torre con tres cubos |
| QDSM7 | - |  |  | SI | 6. (S) Mímica en respuesta al rostro del examinado... |
| QDSM70 | - |  |  | SI | 69. (L) Dice al menos seis palabras |
| QDSM71 | - |  |  | SI | 70. (LS) Usa palabras para comunicar deseos |
| QDSM72 | - |  |  | SI | 71. (M) se para en un pie con ayuda |
| QDSM73 | - |  |  | SI | 72. (L) Nombra dos objetivos de los cuatro present... |
| QDSM74 | - |  |  | SI | 73. (S) Ayuda en tareas simples |
| QDSM75 | - |  |  | SI | 74. (L) Apunta 4 o más partes en el cuerpo de la m... |
| QDSM76 | - |  |  | SI | 75. (C) Construye una torre con cinco cubos |
| QDSM77 | - |  |  | SI | Edad Mental |
| QDSM78 | - |  |  | SI | Edad cronológica |
| QDSM79 | - |  |  | SI | Edad cronológica corregida |
| QDSM8 | - |  |  | SI | 7. (LS) Vocaliza en respuesta a la sonrisa y conve... |
| QDSM80 | - |  |  | SI | Coeficiente desarrollo bruto |
| QDSM81 | - |  |  | SI | Coeficiente desarrollo estándar |
| QDSM82 | - |  |  | SI | Resultado EEDP |
| QDSM82ObsDR | - |  |  | SI | Resultado EEDP DR |
| QDSM83 | - |  |  | SI | Coordinación |
| QDSM84 | - |  |  | SI | Social |
| QDSM85 | - |  |  | SI | Lenguaje |
| QDSM86 | - |  |  | SI | Motora |
| QDSM87 | - |  |  | SI | 54 .- (LS) Entrega como respuesta a una orden |
| QDSM88 | - |  |  | SI | 64.- (C) Retira inmediatamente la pastilla de la b... |
| QDSM9 | - |  |  | SI | 8. (C)(S) Reacciona ante el desaparecimiento de la... |
| QDSM90 | - |  |  | SI | Calcular Razón con Edad cronológica |
| QECE | - |  |  | SI | Cálculo de Edad Cronológica del Paciente |
| QECS | - |  |  | SI | Edad Cronologica en Semanas |
| QEDP | - |  |  | SI | Edad Corregida |
| QMES01 | - |  |  | SI | FECHA01 |
| QMES02 | - |  |  | SI | FECHA02 |
| QMES03 | - |  |  | SI | FECHA03 |
| QMES04 | - |  |  | SI | FECHA04 |
| QMES05 | - |  |  | SI | FECHA05 |
| QMES06 | - |  |  | SI | FECHA06 |
| QMES07 | - |  |  | SI | FECHA07 |
| QMES08 | - |  |  | SI | FECHA08 |
| QMES09 | - |  |  | SI | FECHA09 |
| QMES10 | - |  |  | SI | FECHA10 |
| QMES12 | - |  |  | SI | FECHA12 |
| QMES15 | - |  |  | SI | FECHA15 |
| QMES18 | - |  |  | SI | FECHA18 |
| QMES21 | - |  |  | SI | FECHA21 |
| QMES24 | - |  |  | SI | FECHA24 |
| QOVC | - |  |  | SI | Comentarios |
| QP10M | - |  |  | SI | Puntaje 10 Meses |
| QP12M | - |  |  | SI | Puntaje 12 Meses |
| QP15M | - |  |  | SI | Puntaje 15 Meses |
| QP18M | - |  |  | SI | Puntaje 18 Meses |
| QP1M | - |  |  | SI | Puntaje 1 Mes |
| QP21M | - |  |  | SI | Puntaje 21 Meses |
| QP24M | - |  |  | SI | Puntaje 24 Meses |
| QP2M | - |  |  | SI | Puntaje 2 Meses |
| QP3M | - |  |  | SI | Puntaje 3 Meses |
| QP4M | - |  |  | SI | Puntaje 4 Meses |
| QP5M | - |  |  | SI | Puntaje 5 Meses |
| QP6M | - |  |  | SI | Puntaje 6 Meses |
| QP7M | - |  |  | SI | Puntaje 7 Meses |
| QP8M | - |  |  | SI | Puntaje 8 Meses |
| QP9M | - |  |  | SI | Puntaje 9 Meses |
| QREMEC | - |  |  | SI | Razón (EM/EC) |
| QRES10M | - |  |  | SI | Resultado 10 Meses |
| QRES12M | - |  |  | SI | Resultado 12 Meses |
| QRES15M | - |  |  | SI | Resultado 15 Meses |
| QRES18M | - |  |  | SI | Resultado 18 Meses |
| QRES1M | - |  |  | SI | Resultado 1 Mes |
| QRES21M | - |  |  | SI | Resultado 21 Meses |
| QRES24M | - |  |  | SI | Resultado 24 Meses |
| QRES2M | - |  |  | SI | Resultado 2 Meses |
| QRES3M | - |  |  | SI | Resultado 3 Meses |
| QRES4M | - |  |  | SI | Resultado 4 Meses |
| QRES5M | - |  |  | SI | Resultado 5 Meses |
| QRES6M | - |  |  | SI | Resultado 6 Meses |
| QRES7M | - |  |  | SI | Resultado 7 Meses |
| QRES8M | - |  |  | SI | Resultado 8 Meses |
| QRES9M | - |  |  | SI | Resultado 9 Meses |
| QROV | - |  |  | SI | Otra Vulnerabilidad |
| QSB | - |  |  | SI | Selección de Baremo |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*