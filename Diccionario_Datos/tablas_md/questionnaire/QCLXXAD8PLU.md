# questionnaire.QCLXXAD8PLU

> AD8PLUS

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile. *(AD8PLUS)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | varchar |  |  | SI | Record ID |
| Q03 | varchar |  |  | SI | Responsable |
| Q04 | varchar |  |  | SI | ¿A quién se le aplica? |
| Q05 | varchar |  |  | SI | Otros |
| Q06 | varchar |  |  | SI | 1. ¿Usted decidió traerlo/a a consultar por sus pr... |
| Q07 | varchar |  |  | SI | 2. ¿Actualmente se queja de sus problemas de memor... |
| Q08 | varchar |  |  | SI | 3. ¿Existen cambios en la capacidad de evaluar ade... |
| Q09 | varchar |  |  | SI | [ Marcar SÍ en elcaso que existan cambios en relac... |
| Q10 | varchar |  |  | SI | 4. En comparación a años anteriores, ¿el paciente ... |
| Q11 | varchar |  |  | SI | 5. ¿El paciente se desorienta en el espacio o se c... |
| Q12 | varchar |  |  | SI | 6. ¿En el último tiempo, el paciente repite frecue... |
| Q13 | varchar |  |  | SI | 7. Con respecto a años anteriores, ¿el paciente pi... |
| Q14 | varchar |  |  | SI | 8. Con respecto a años anteriores, ¿presenta dific... |
| Q15 | varchar |  |  | SI | 9. En el último tiempo, ¿el paciente anota lo que ... |
| Q16 | varchar |  |  | SI | 10. En comparación con años anteriores, ¿el pacien... |
| Q17 | varchar |  |  | SI | 11. ¿Presenta un problema persistente de la memori... |
| Q18 | varchar |  |  | SI | 13. Con respecto a años anteriores, ¿comente error... |
| Q19 | varchar |  |  | SI | 14. Con respecto a años anteriores, ¿tiene dificul... |
| Q20 | varchar |  |  | SI | 15. ¿Dejó de trabajar debido a sus problemas de me... |
| Q21 | varchar |  |  | SI | 16. Con respecto a años anteriores, ¿actualmente t... |
| Q22 | varchar |  |  | SI | 17. ¿Tiene dificultades para manejar sin ayuda su ... |
| Q23 | varchar |  |  | SI | 18. ¿Tiene dificultades para hacer una llamada por... |
| Q24 | varchar |  |  | SI | 19. ¿Tiene dificultades para movilizarse solo en e... |
| Q25 | varchar |  |  | SI | 20. Con respecto a años anteriores,¿tiene dificult... |
| Q26 | varchar |  |  | SI | 21. En el último tiempo, ¿las dificultades del pac... |
| Q27 | varchar |  |  | SI | 22. En el último tiempo, ¿Se siente triste la mayo... |
| Q28 | varchar |  |  | SI | 23. ¿Prefiere quedarse en casa y/o ha perdido inte... |
| Q29 | varchar |  |  | SI | 24. ¿Siente que su situación no tiene vuelta? |
| Q30 | varchar |  |  | SI | 25. ¿El paciente se siente nervioso o muy sangusti... |
| Q31 | varchar |  |  | SI | 26. ¿Con respecto a años anteriores, ¿se molesta o... |
| Q32 | varchar |  |  | SI | 27. ¿Suele sentirse sin energía? |
| Q33 | varchar |  |  | SI | 28. ¿Ha presentado cambios en su apetito o peso? |
| Q34 | varchar |  |  | SI | 29. En el último tiempo, ¿se siente desamparado y ... |
| Q35 | varchar |  |  | SI | 30. En comparación a años anteriores, ¿tiene dific... |
| Q36 | varchar |  |  | SI | 12. En comparación a años anteriores ¿está más des... |
| Q37 | varchar |  |  | SI | Observaciones |
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