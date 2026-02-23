# SQLUser.PA_ORAnaestMethodTypeSnapshot

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAATYPE_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAATYPE_ChildSub | double |  |  | NO | Childsub |
| PAATYPE_RowId | varchar |  |  | NO | - |
| PAATYPE_Type_DR | bigint |  | FK | SI | Des Ref ORCVentilationMode |
| Q01 | - |  |  | SI | Iniciales del Nombres y Apellidos |
| Q02 | - |  |  | SI | Fecha de Nacimiento |
| Q03 | - |  |  | SI | Fecha de Evaluación |
| Q04 | - |  |  | SI | 1. ¿Tiene alguna dificultad para dar un paseo cort... |
| Q05 | - |  |  | SI | 2. ¿Tiene que permanecer en cama o sentado/a en un... |
| Q06 | - |  |  | SI | 3. ¿Necesita ayuda para comer, vestirse, asearse o... |
| Q07 | - |  |  | SI | Durante la semana pasada |
| Q08 | - |  |  | SI | 4. ¿Se quedó sin aliento? |
| Q09 | - |  |  | SI | 5. ¿Tuvo algún dolor? |
| Q10 | - |  |  | SI | 6. ¿Tuvo dificultades para dormir? |
| Q11 | - |  |  | SI | 7. ¿Se sintió débil? |
| Q12 | - |  |  | SI | 8. ¿Se sintió sin apetito? |
| Q13 | - |  |  | SI | 9. ¿Sintió náuseas? |
| Q14 | - |  |  | SI | 10. ¿Tuvo estreñimiento? |
| Q15 | - |  |  | SI | 11. ¿Se sintió cansado/a? |
| Q16 | - |  |  | SI | 12. ¿Interfirió algún dolor en sus actividades dia... |
| Q17 | - |  |  | SI | 13. ¿Se sintió nervioso/a? |
| Q18 | - |  |  | SI | 14. ¿Se sintió deprimido/a? |
| Q19 | - |  |  | SI | 15. ¿En general, ¿cómo valoraría su calidad de vid... |
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