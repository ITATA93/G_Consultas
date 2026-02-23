# SQLUser.MRC_ObservationItemExtCodes

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXTCODE_ParRef | bigint | PK |  | NO | MRC_ObservationItem Parent Reference |
| EXTCODE_Childsub | double |  |  | NO | Childsub |
| EXTCODE_Code | varchar |  |  | NO | Code |
| EXTCODE_CreatedDate | date |  |  | SI | Created Date |
| EXTCODE_CreatedTime | time |  |  | SI | Created Time |
| EXTCODE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXTCODE_DateFrom | date |  |  | SI | Date From  |
| EXTCODE_DateTo | date |  |  | SI | Date To |
| EXTCODE_Desc | varchar |  |  | NO | Description |
| EXTCODE_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| EXTCODE_RowId | varchar |  |  | NO | - |
| EXTCODE_UpdatedDate | date |  |  | SI | Updated Date |
| EXTCODE_UpdatedTime | time |  |  | SI | Updated Time |
| EXTCODE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Què hacìas antes de ingresar al centro |
| Q02 | - |  |  | SI | Cuàles eran tus responsabilidades en lo que hacìas |
| Q03 | - |  |  | SI | Te gustaba lo que hacìas |
| Q04 | - |  |  | SI | Las personas cercanas a ti, valoraban lo que hacìa... |
| Q05 | - |  |  | SI | Has realizado alguna actividad de la cual  te sien... |
| Q06 | - |  |  | SI | Aparte de tu (trabajo, estudio) tienes otras respo... |
| Q07 | - |  |  | SI | Cuàles |
| Q08 | - |  |  | SI | Crees que las actividades que realizabas se vieron... |
| Q09 | - |  |  | SI | De què manera |
| Q10 | - |  |  | SI | Describe un dìa durante la semana y señala las dif... |
| Q11 | - |  |  | SI | Si llegaras a tener un dìa realmente bueno o realm... |
| Q12 | - |  |  | SI | Como era tu rutina, hasta seis meses antes de ingr... |
| Q13 | - |  |  | SI | Cuàles son las diferencias respecto de tu rutina a... |
| Q14 | - |  |  | SI | Què es lo que màs te gustarìa cambiar de tu rutina |
| Q15 | - |  |  | SI | Què es lo que mantendrìas de tu |
| Q16 | - |  |  | SI | Què cosas haces para divertirte o relajarte |
| Q17 | - |  |  | SI | Cuàles te gustarìa realizar |
| Q18 | - |  |  | SI | Què actividades de tiempo libre realizas |
| Q19 | - |  |  | SI | Con quiènes te diviertes o relajas |
| Q20 | - |  |  | SI | Cuàles han sido los eventos o experiencias que màs... |
| Q21 | - |  |  | SI | Cuàndo consideras tù que las cosas en tu vida han ... |
| Q22 | - |  |  | SI | Què cosas hiciste tù que permitieron que las cosas... |
| Q23 | - |  |  | SI | Cuàles consideras tù que es el mayor èxito en tu v... |
| Q24 | - |  |  | SI | Cuàl crees que ha sido el mayor fracaso en tu vida |
| Q25 | - |  |  | SI | Què cosas te ves haciendo en el futuro |
| Q26 | - |  |  | SI | Còmo es el lugar donde vives |
| Q27 | - |  |  | SI | Estàs conforme con el lugar donde vives, ¿Què camb... |
| Q28 | - |  |  | SI | Quiènes son las personas mas importantes en tu vid... |
| Q29 | - |  |  | SI | En caso de necesitar ayuda,con que persona(s) cuen... |
| Q30 | - |  |  | SI | Què tipo de ayuda podrìas recibir de estas persona... |
| Q31 | - |  |  | SI | Còmo es el lugar donde trabajas o estudias |
| Q32 | - |  |  | SI | Estàs conforme con el lugar donde trabajas o estud... |
| Q33 | - |  |  | SI | Còmo te llevas con tus jefes y compañeros de traba... |
| Q34 | - |  |  | SI | Cuàles son algunas de las cosas que consideras imp... |
| Q35 | - |  |  | SI | Te ha sido posible en tu vida escoger las cosas im... |
| Q36 | - |  |  | SI | Cuàl es el principal desafìo que enfrentas actualm... |
| Q37 | - |  |  | SI | Què metas te planteas hoy para tu futuro |
| Q38 | - |  |  | SI | Cuàles son las principales aprehensiones o miedos ... |
| Q39 | - |  |  | SI | Con què recursos cuentas para cumplir tus objetivo... |
| Q40 | - |  |  | SI | Què cosas piensas hacer para mejorar tu vida |
| Q41 | - |  |  | SI | Cuàl es tu estado de salud actual |
| Q42 | - |  |  | SI | Tienes alguna enfermedad crònica, ¿Desde cuàndo? |
| Q43 | - |  |  | SI | Posee alguna enfermedad psiquiàtrica, ¿Te estàs tr... |
| Q44 | - |  |  | SI | Posees algùn tipo de discapacidad fìsica, ¿Conside... |
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