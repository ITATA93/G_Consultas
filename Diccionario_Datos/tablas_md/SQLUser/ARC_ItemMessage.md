# SQLUser.ARC_ItemMessage

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MESS_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| MESS_AgeFrom | double |  |  | SI | Age From |
| MESS_AgeTo | double |  |  | SI | Age To |
| MESS_Childsub | double |  |  | NO | Childsub |
| MESS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MESS_CreatedDate | date |  |  | SI | Created Date |
| MESS_CreatedTime | time |  |  | SI | Created Time |
| MESS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MESS_Message | varchar |  |  | SI | Message |
| MESS_RowId | varchar |  |  | NO | - |
| MESS_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| MESS_UpdatedDate | date |  |  | SI | Updated Date |
| MESS_UpdatedTime | time |  |  | SI | Updated Time |
| MESS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Record ID |
| Q03 | - |  |  | SI | Responsable |
| Q04 | - |  |  | SI | ¿A quién se le aplica? |
| Q05 | - |  |  | SI | Otros |
| Q06 | - |  |  | SI | 1. ¿Usted decidió traerlo/a a consultar por sus pr... |
| Q07 | - |  |  | SI | 2. ¿Actualmente se queja de sus problemas de memor... |
| Q08 | - |  |  | SI | 3. ¿Existen cambios en la capacidad de evaluar ade... |
| Q09 | - |  |  | SI | [ Marcar SÍ en elcaso que existan cambios en relac... |
| Q10 | - |  |  | SI | 4. En comparación a años anteriores, ¿el paciente ... |
| Q11 | - |  |  | SI | 5. ¿El paciente se desorienta en el espacio o se c... |
| Q12 | - |  |  | SI | 6. ¿En el último tiempo, el paciente repite frecue... |
| Q13 | - |  |  | SI | 7. Con respecto a años anteriores, ¿el paciente pi... |
| Q14 | - |  |  | SI | 8. Con respecto a años anteriores, ¿presenta dific... |
| Q15 | - |  |  | SI | 9. En el último tiempo, ¿el paciente anota lo que ... |
| Q16 | - |  |  | SI | 10. En comparación con años anteriores, ¿el pacien... |
| Q17 | - |  |  | SI | 11. ¿Presenta un problema persistente de la memori... |
| Q18 | - |  |  | SI | 13. Con respecto a años anteriores, ¿comente error... |
| Q19 | - |  |  | SI | 14. Con respecto a años anteriores, ¿tiene dificul... |
| Q20 | - |  |  | SI | 15. ¿Dejó de trabajar debido a sus problemas de me... |
| Q21 | - |  |  | SI | 16. Con respecto a años anteriores, ¿actualmente t... |
| Q22 | - |  |  | SI | 17. ¿Tiene dificultades para manejar sin ayuda su ... |
| Q23 | - |  |  | SI | 18. ¿Tiene dificultades para hacer una llamada por... |
| Q24 | - |  |  | SI | 19. ¿Tiene dificultades para movilizarse solo en e... |
| Q25 | - |  |  | SI | 20. Con respecto a años anteriores,¿tiene dificult... |
| Q26 | - |  |  | SI | 21. En el último tiempo, ¿las dificultades del pac... |
| Q27 | - |  |  | SI | 22. En el último tiempo, ¿Se siente triste la mayo... |
| Q28 | - |  |  | SI | 23. ¿Prefiere quedarse en casa y/o ha perdido inte... |
| Q29 | - |  |  | SI | 24. ¿Siente que su situación no tiene vuelta? |
| Q30 | - |  |  | SI | 25. ¿El paciente se siente nervioso o muy sangusti... |
| Q31 | - |  |  | SI | 26. ¿Con respecto a años anteriores, ¿se molesta o... |
| Q32 | - |  |  | SI | 27. ¿Suele sentirse sin energía? |
| Q33 | - |  |  | SI | 28. ¿Ha presentado cambios en su apetito o peso? |
| Q34 | - |  |  | SI | 29. En el último tiempo, ¿se siente desamparado y ... |
| Q35 | - |  |  | SI | 30. En comparación a años anteriores, ¿tiene dific... |
| Q36 | - |  |  | SI | 12. En comparación a años anteriores ¿está más des... |
| Q37 | - |  |  | SI | Observaciones |
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