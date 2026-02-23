# questionnaire.QTCEDESSPSI

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ1 | varchar | PK |  | SI | - |
| CQ10 | varchar | PK |  | SI | - |
| CQ11 | varchar | PK |  | SI | - |
| CQ12 | varchar | PK |  | SI | - |
| CQ13 | varchar | PK |  | SI | - |
| CQ14 | varchar | PK |  | SI | - |
| CQ15 | varchar | PK |  | SI | - |
| CQ16 | varchar | PK |  | SI | - |
| CQ17 | varchar | PK |  | SI | - |
| CQ18 | varchar | PK |  | SI | - |
| CQ19 | varchar | PK |  | SI | - |
| CQ2 | varchar | PK |  | SI | - |
| CQ20 | varchar | PK |  | SI | - |
| CQ3 | varchar | PK |  | SI | - |
| CQ4 | varchar | PK |  | SI | - |
| CQ5 | varchar | PK |  | SI | - |
| CQ6 | varchar | PK |  | SI | - |
| CQ7 | varchar | PK |  | SI | - |
| CQ8 | varchar | PK |  | SI | - |
| CQ9 | varchar | PK |  | SI | - |
| CQACTEV | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q1 | varchar | PK |  | SI | (C) 1. Levanta la cabeza y hombros al ser llevado ... |
| Q10 | varchar | PK |  | SI | (C) 10. Espontáneamente garabatea   |
| Q11 | varchar | PK |  | SI | (C) 13. Arma una torre de cuatro cubos |
| Q12 | varchar | PK |  | SI | (L) 11. mita tres palabras   |
| Q13 | varchar | PK |  | SI | (LS) 12. Muestra lo que desea, apuntándolo   |
| Q14 | varchar | PK |  | SI | (L) 14. Nombra un objeto de los cuatro presentados |
| Q15 | varchar | PK |  | SI | (M) 15. Se para en un pie con apoyo |
| Q16 | varchar | PK |  | SI | (CS) 16. Usa cuchara |
| Q17 | varchar | PK |  | SI | (M) 17. Se para en un pie sin apoyo un segundo |
| Q18 | varchar | PK |  | SI | (C) 18. Desata cordones |
| Q19 | varchar | PK |  | SI | (L) 19. Nombra 2 objetos de los 4 presentados |
| Q2 | varchar | PK |  | SI | (M) 2. Gira la cabeza al sonido de la campanilla   |
| Q20 | varchar | PK |  | SI | (S) 20. Ayuda en tareas simples |
| Q21 | varchar | PK |  | SI | Resultado |
| Q3 | varchar | PK |  | SI | (LS) 3. Ríe a carcajadas   |
| Q4 | varchar | PK |  | SI | (C) 4. La cabeza sigue la cuchara que desaparece   |
| Q5 | varchar | PK |  | SI | (M) 5.Camina afirmado de una mano   |
| Q6 | varchar | PK |  | SI | (C) 6. Aplaude   |
| Q7 | varchar | PK |  | SI | (L) 7. Dice al menos 2 palabras con sentido   |
| Q8 | varchar | PK |  | SI | (LS) 8. Entrega como respuesta a una orden   |
| Q9 | varchar | PK |  | SI | (M) 9. Camina solo   |
| QACTEV | varchar | PK |  | SI | Esta evaluación corrresponde a: |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*