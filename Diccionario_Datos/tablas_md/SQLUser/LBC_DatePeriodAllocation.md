# SQLUser.LBC_DatePeriodAllocation

**Schema:** SQLUser
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDPA_RowID | bigint | PK |  | NO | - |
| LBCDPA_CreatedDate | date |  |  | SI | Created Date |
| LBCDPA_CreatedTime | time |  |  | SI | Created Time |
| LBCDPA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDPA_DateFrom | date |  |  | SI | Effective date for the record |
| LBCDPA_DateTo | date |  |  | SI | Last day the record is active  |
| LBCDPA_ObjectReference | varchar |  |  | SI | - |
| LBCDPA_ReportPage_DR | bigint |  | FK | SI | Report Page |
| LBCDPA_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDPA_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDPA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nombre de la madre |
| Q02 | - |  |  | SI | Colegio |
| Q03 | - |  |  | SI | Curso |
| Q04 | - |  |  | SI | Peso |
| Q04ObsDR | - |  |  | SI | Peso DR |
| Q05 | - |  |  | SI | Talla |
| Q05ObsDR | - |  |  | SI | Talla DR |
| Q06 | - |  |  | SI | IMC (Calculado) |
| Q07 | - |  |  | SI | Circunferencia Abdominal |
| Q07ObsDR | - |  |  | SI | Circunferencia Abdominal  DR |
| Q08 | - |  |  | SI | Percentil IMC - Edad |
| Q08ObsDR | - |  |  | SI | Percentil IMC - Edad  DR |
| Q09 | - |  |  | SI | Percentil Talla - Edad |
| Q09ObsDR | - |  |  | SI | Percentil Talla - Edad  DR |
| Q10 | - |  |  | SI | Percentil de Circunferencia Abdominal |
| Q10ObsDR | - |  |  | SI | Percentil de Circunferencia Abdominal  DR |
| Q11 | - |  |  | SI | Tanner Mamas |
| Q11ObsDR | - |  |  | SI | Tanner Mamas  DR |
| Q12 | - |  |  | SI | Tanner Vello Púbico |
| Q12ObsDR | - |  |  | SI | Tanner Vello Púbico  DR |
| Q13 | - |  |  | SI | 1. ¿No controla el pipi de día o de noche, aunque ... |
| Q14 | - |  |  | SI | 2. ¿Se queja de dolor frecuente al hacer pipi? |
| Q15 | - |  |  | SI | 3. ¿No controla las deposiciones (caca) de día o d... |
| Q16 | - |  |  | SI | 4. ¿Actualmente posee parásitos (gusanos) en sus d... |
| Q17 | - |  |  | SI | 5. ¿Mancha los calzones con secreción o deposicion... |
| Q18 | - |  |  | SI | 6. ¿Tiene picazón anal frecuente? |
| Q19 | - |  |  | SI | 7. ¿Tiene secreación de muy mal olor en genitales,... |
| Q20 | - |  |  | SI | 8. ¿Tiene un aumento de volumen (hinchazón) en la ... |
| Q21 | - |  |  | SI | 9. ¿Tiene olor axilar similar al de un adulto (Est... |
| Q22 | - |  |  | SI | 10. ¿Ha tenido sibilancias o silbido al pecho en e... |
| Q23 | - |  |  | SI | 11. ¿Ha tenido sibilancias o silbido al pecho dura... |
| Q24 | - |  |  | SI | 12. ¿Ronca de noche? |
| Q25 | - |  |  | SI | 13. Si ronca de noche ¿Tiene pausas respiratorias?... |
| Q26 | - |  |  | SI | 14. ¿Tiene actualmente piojos en su pelo? |
| Q27 | - |  |  | SI | 15. ¿Ha tenido su primera menstruación? |
| Q28 | - |  |  | SI | Si tuvo menstruación, indique la edad cumplida en ... |
| Q29 | - |  |  | SI | Indique alguna inquietud que tenga al respecto a l... |
| Q30 | - |  |  | SI | Perímetro de Cintura |
| Q30ObsDR | - |  |  | SI | Perímetro de Cintura DR |
| Q31 | - |  |  | SI | IMC por Edad |
| Q31ObsDR | - |  |  | SI | IMC por Edad DR |
| Q32 | - |  |  | SI | Peso por Edad |
| Q32ObsDR | - |  |  | SI | Peso por Edad DR |
| Q33 | - |  |  | SI | Talla por Edad |
| Q33ObsDR | - |  |  | SI | Talla por Edad DR |
| Q34 | - |  |  | SI | Puntaje Z IMC por Edad |
| Q34ObsDR | - |  |  | SI | Puntaje Z IMC por Edad DR |
| Q35 | - |  |  | SI | Puntaje Z Peso por Edad |
| Q35ObsDR | - |  |  | SI | Puntaje Z Peso por Edad DR |
| Q36 | - |  |  | SI | Puntaje Z Talla por Edad |
| Q36ObsDR | - |  |  | SI | Puntaje Z Talla por Edad DR |
| Q37 | - |  |  | SI | Calificación Estatura |
| Q37ObsDR | - |  |  | SI | Calificación Estatura DR |
| Q38 | - |  |  | SI | Estatura Padre |
| Q38ObsDR | - |  |  | SI | Estatura Padre DR |
| Q39 | - |  |  | SI | Estatura Madre |
| Q39ObsDR | - |  |  | SI | Estatura Madre DR |
| Q40 | - |  |  | SI | Talla Diana Hombres |
| Q41 | - |  |  | SI | Talla Diana Mujeres |
| Q42 | - |  |  | SI | Diagnóstico Nutricional |
| Q42ObsDR | - |  |  | SI | Diagnóstico Nutricional DR |
| Q43 | - |  |  | SI | Obesidad Abdominal según Cirunferencia de Cintura |
| Q43ObsDR | - |  |  | SI | Obesidad Abdominal según Cirunferencia de Cintura ... |
| Q44 | - |  |  | SI | Índice Cintura/Estatura |
| Q45 | - |  |  | SI | Ingresar Información en forma manual |
| Q46 | - |  |  | SI | Corregir cálculos según edad biológica |
| Q47 | - |  |  | SI | Años |
| Q48 | - |  |  | SI | Meses |
| Q49 | - |  |  | SI | Ingrese edad biológica estimada |
| Q50 | - |  |  | SI | P.A. Sistólica |
| Q50ObsDR | - |  |  | SI | P.A. Sistólica DR |
| Q51 | - |  |  | SI | P.A. Diastólica |
| Q51ObsDR | - |  |  | SI | P.A. Diastólica DR |
| Q52 | - |  |  | SI | Percentil PAS |
| Q53 | - |  |  | SI | Percentil PAD |
| QNNA01E | - |  |  | SI | Curso [REM] |
| QPNN | - |  |  | SI | Paciente NANEAS |
| QSEN | - |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
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