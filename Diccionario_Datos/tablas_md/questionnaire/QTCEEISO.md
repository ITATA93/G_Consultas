# questionnaire.QTCEEISO

> Entrevista para la Integración Socio Ocupacional

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Entrevista para la Integración Socio Ocupacional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Què hacìas antes de ingresar al centro |
| Q02 | varchar |  |  | SI | Cuàles eran tus responsabilidades en lo que hacìas |
| Q03 | varchar |  |  | SI | Te gustaba lo que hacìas |
| Q04 | varchar |  |  | SI | Las personas cercanas a ti, valoraban lo que hacìa... |
| Q05 | varchar |  |  | SI | Has realizado alguna actividad de la cual  te sien... |
| Q06 | varchar |  |  | SI | Aparte de tu (trabajo, estudio) tienes otras respo... |
| Q07 | varchar |  |  | SI | Cuàles |
| Q08 | varchar |  |  | SI | Crees que las actividades que realizabas se vieron... |
| Q09 | varchar |  |  | SI | De què manera |
| Q10 | varchar |  |  | SI | Describe un dìa durante la semana y señala las dif... |
| Q11 | varchar |  |  | SI | Si llegaras a tener un dìa realmente bueno o realm... |
| Q12 | varchar |  |  | SI | Como era tu rutina, hasta seis meses antes de ingr... |
| Q13 | varchar |  |  | SI | Cuàles son las diferencias respecto de tu rutina a... |
| Q14 | varchar |  |  | SI | Què es lo que màs te gustarìa cambiar de tu rutina... |
| Q15 | varchar |  |  | SI | Què es lo que mantendrìas de tu  |
| Q16 | varchar |  |  | SI | Què cosas haces para divertirte o relajarte |
| Q17 | varchar |  |  | SI | Cuàles te gustarìa realizar |
| Q18 | varchar |  |  | SI | Què actividades de tiempo libre realizas |
| Q19 | varchar |  |  | SI | Con quiènes te diviertes o relajas |
| Q20 | varchar |  |  | SI | Cuàles han sido los eventos o experiencias que màs... |
| Q21 | varchar |  |  | SI | Cuàndo consideras tù que las cosas en tu vida han ... |
| Q22 | varchar |  |  | SI | Què cosas hiciste tù que permitieron que las cosas... |
| Q23 | varchar |  |  | SI | Cuàles consideras tù que es el mayor èxito en tu v... |
| Q24 | varchar |  |  | SI | Cuàl crees que ha sido el mayor fracaso en tu vida |
| Q25 | varchar |  |  | SI | Què cosas te ves haciendo en el futuro |
| Q26 | varchar |  |  | SI | Còmo es el lugar donde vives |
| Q27 | varchar |  |  | SI | Estàs conforme con el lugar donde vives, ¿Què camb... |
| Q28 | varchar |  |  | SI | Quiènes son las personas mas importantes en tu vid... |
| Q29 | varchar |  |  | SI | En caso de necesitar ayuda,con que persona(s) cuen... |
| Q30 | varchar |  |  | SI | Què tipo de ayuda podrìas recibir de estas persona... |
| Q31 | varchar |  |  | SI | Còmo es el lugar donde trabajas o estudias |
| Q32 | varchar |  |  | SI | Estàs conforme con el lugar donde trabajas o estud... |
| Q33 | varchar |  |  | SI | Còmo te llevas con tus jefes y compañeros de traba... |
| Q34 | varchar |  |  | SI | Cuàles son algunas de las cosas que consideras imp... |
| Q35 | varchar |  |  | SI | Te ha sido posible en tu vida escoger las cosas im... |
| Q36 | varchar |  |  | SI | Cuàl es el principal desafìo que enfrentas actualm... |
| Q37 | varchar |  |  | SI | Què metas te planteas hoy para tu futuro |
| Q38 | varchar |  |  | SI | Cuàles son las principales aprehensiones o miedos ... |
| Q39 | varchar |  |  | SI | Con què recursos cuentas para cumplir tus objetivo... |
| Q40 | varchar |  |  | SI | Què cosas piensas hacer para mejorar tu vida |
| Q41 | varchar |  |  | SI | Cuàl es tu estado de salud actual |
| Q42 | varchar |  |  | SI | Tienes alguna enfermedad crònica, ¿Desde cuàndo? |
| Q43 | varchar |  |  | SI | Posee alguna enfermedad psiquiàtrica, ¿Te estàs tr... |
| Q44 | varchar |  |  | SI | Posees algùn tipo de discapacidad fìsica, ¿Conside... |
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