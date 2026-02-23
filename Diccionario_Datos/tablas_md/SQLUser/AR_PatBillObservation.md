# SQLUser.AR_PatBillObservation

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBS_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| OBS_Childsub | double |  |  | NO | Childsub |
| OBS_Date | date |  |  | SI | Date |
| OBS_ObservValueMultiLineText | varchar |  |  | SI | Observation Value Multi Line Text |
| OBS_ObservationCode | varchar |  |  | SI | Observation Code |
| OBS_ObservationType_DR | bigint |  | FK | SI | Des Ref to ARCObservationType |
| OBS_ObservationValue | varchar |  |  | SI | Observation Value |
| OBS_ObservationValueText | varchar |  |  | SI | Observation Value Text |
| OBS_RowId | varchar |  |  | NO | - |
| OBS_Time | time |  |  | SI | Time |
| Q01 | - |  |  | SI | 1. ¿Disfruta su niño cuando lo balancea o hacen sa... |
| Q02 | - |  |  | SI | 2. ¿Se interesa su niño por otros niños o niñas? |
| Q03 | - |  |  | SI | 3. ¿Le gusta a su niño subirse a las cosas, por ej... |
| Q04 | - |  |  | SI | 4. ¿Disfruta su niño jugando al ahí está (juegos e... |
| Q05 | - |  |  | SI | 5. ¿Le gusta a su niño simular que habla por teléf... |
| Q06 | - |  |  | SI | 6. ¿Utiliza su niño su dedo índice para señalar al... |
| Q07 | - |  |  | SI | 7. ¿Usa su niño su dedo índice para señalar algo o... |
| Q08 | - |  |  | SI | 8. ¿Puede su niño jugar bien con juguetes pequeños... |
| Q09 | - |  |  | SI | 9. ¿Le trae su niño a usted (padre o madre) objeto... |
| Q10 | - |  |  | SI | 10. ¿Lo mira su niño directamente a los ojos por m... |
| Q11 | - |  |  | SI | 11. ¿Parece su niño demasiado sensitivo al ruido (... |
| Q12 | - |  |  | SI | 12. ¿Sonríe su niño en respuesta a su cara o a su ... |
| Q13 | - |  |  | SI | 13. ¿Lo imita su niño? Por ejemplo, si usted le ha... |
| Q14 | - |  |  | SI | 14. ¿Responde su niño a su nombre cuando lo llama? |
| Q15 | - |  |  | SI | 15. Si usted señala un juguete que está al otro la... |
| Q16 | - |  |  | SI | 16. ¿Ha aprendido a caminar su niño? |
| Q17 | - |  |  | SI | 17. ¿Presta atención su niño atención a las cosas ... |
| Q18 | - |  |  | SI | 18. ¿Hace su niño movimientos raros con los dedos ... |
| Q19 | - |  |  | SI | 19. ¿Trata su niño de llamar la atención sobre las... |
| Q20 | - |  |  | SI | 20. ¿se ha preguntado alguna vez si su niño es sor... |
| Q21 | - |  |  | SI | 21. ¿Comprende lo que otros le dicen? |
| Q22 | - |  |  | SI | 22. ¿Fija su niño su mirada en nada o camina sin s... |
| Q23 | - |  |  | SI | 23. ¿Su niño mira a su cara para comprobar su reac... |
| Q24 | - |  |  | SI | Llenado por |
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