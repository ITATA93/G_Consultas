# questionnaire.QCLXXMCHAT

> M-CHAT: Lista de Verificación para el Autismo en Niños Pequeños, Modificada

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* M-CHAT: Lista de Verificación para el Autismo en Niños Pequeños, Modificada

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. ¿Disfruta su niño cuando lo balancea o hacen sa... |
| Q02 | varchar |  |  | SI | 2. ¿Se interesa su niño por otros niños o niñas? |
| Q03 | varchar |  |  | SI | 3. ¿Le gusta a su niño subirse a las cosas, por ej... |
| Q04 | varchar |  |  | SI | 4. ¿Disfruta su niño jugando al ahí está (juegos e... |
| Q05 | varchar |  |  | SI | 5. ¿Le gusta a su niño simular que habla por teléf... |
| Q06 | varchar |  |  | SI | 6. ¿Utiliza su niño su dedo índice para señalar al... |
| Q07 | varchar |  |  | SI | 7. ¿Usa su niño su dedo índice para señalar algo o... |
| Q08 | varchar |  |  | SI |  8. ¿Puede su niño jugar bien con juguetes pequeño... |
| Q09 | varchar |  |  | SI | 9. ¿Le trae su niño a usted (padre o madre) objeto... |
| Q10 | varchar |  |  | SI | 10. ¿Lo mira su niño directamente a los ojos por m... |
| Q11 | varchar |  |  | SI | 11. ¿Parece su niño demasiado sensitivo al ruido (... |
| Q12 | varchar |  |  | SI | 12. ¿Sonríe su niño en respuesta a su cara o a su ... |
| Q13 | varchar |  |  | SI | 13. ¿Lo imita su niño? Por ejemplo, si usted le ha... |
| Q14 | varchar |  |  | SI | 14. ¿Responde su niño a su nombre cuando lo llama? |
| Q15 | varchar |  |  | SI | 15. Si usted señala un juguete que está al otro la... |
| Q16 | varchar |  |  | SI | 16. ¿Ha aprendido a caminar su niño? |
| Q17 | varchar |  |  | SI | 17. ¿Presta atención su niño atención a las cosas ... |
| Q18 | varchar |  |  | SI | 18. ¿Hace su niño movimientos raros con los dedos ... |
| Q19 | varchar |  |  | SI | 19. ¿Trata su niño de llamar la atención sobre las... |
| Q20 | varchar |  |  | SI | 20. ¿se ha preguntado alguna vez si su niño es sor... |
| Q21 | varchar |  |  | SI | 21. ¿Comprende lo que otros le dicen? |
| Q22 | varchar |  |  | SI | 22. ¿Fija su niño su mirada en nada o camina sin s... |
| Q23 | varchar |  |  | SI |  23. ¿Su niño mira a su cara para comprobar su rea... |
| Q24 | varchar |  |  | SI |  Llenado por  |
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