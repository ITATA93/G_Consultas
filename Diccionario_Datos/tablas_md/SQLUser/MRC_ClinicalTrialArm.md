# SQLUser.MRC_ClinicalTrialArm

**Schema:** SQLUser
**Columnas:** 284
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARM_ParRef | bigint | PK |  | NO | Parent Reference |
| ARM_Childsub | double |  |  | NO | Childsub |
| ARM_Code | varchar |  |  | NO | Code |
| ARM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARM_CreatedDate | date |  |  | SI | Created Date |
| ARM_CreatedTime | time |  |  | SI | Created Time |
| ARM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARM_DateFrom | date |  |  | SI | Date From |
| ARM_DateTo | date |  |  | SI | Date To |
| ARM_Desc | varchar |  |  | NO | Description |
| ARM_RowId | varchar |  |  | NO | - |
| ARM_UpdatedDate | date |  |  | SI | Updated Date |
| ARM_UpdatedTime | time |  |  | SI | Updated Time |
| ARM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQBYAD | - |  |  | SI | (null) |
| CQBYAI | - |  |  | SI | (null) |
| CQCATD | - |  |  | SI | (null) |
| CQCATI | - |  |  | SI | (null) |
| CQCL | - |  |  | SI | (null) |
| CQCRT | - |  |  | SI | (null) |
| CQFCCD | - |  |  | SI | (null) |
| CQFCCI | - |  |  | SI | (null) |
| CQGLCD | - |  |  | SI | (null) |
| CQGLCI | - |  |  | SI | (null) |
| CQHB | - |  |  | SI | (null) |
| CQHB1 | - |  |  | SI | (null) |
| CQHDL | - |  |  | SI | (null) |
| CQLDL | - |  |  | SI | (null) |
| CQMACT | - |  |  | SI | (null) |
| CQMACTVT | - |  |  | SI | (null) |
| CQMC | - |  |  | SI | (null) |
| CQMCPD | - |  |  | SI | (null) |
| CQMCPI | - |  |  | SI | (null) |
| CQPPAD | - |  |  | SI | (null) |
| CQPPAI | - |  |  | SI | (null) |
| CQPRT | - |  |  | SI | (null) |
| CQRAAD | - |  |  | SI | (null) |
| CQRAAI | - |  |  | SI | (null) |
| CQRMAD | - |  |  | SI | (null) |
| CQRMAI | - |  |  | SI | (null) |
| CQRPNPD | - |  |  | SI | (null) |
| CQRPNPI | - |  |  | SI | (null) |
| CQRPP1D | - |  |  | SI | (null) |
| CQRPP1I | - |  |  | SI | (null) |
| CQSVAD | - |  |  | SI | (null) |
| CQSVAI | - |  |  | SI | (null) |
| CQTDM | - |  |  | SI | (null) |
| CQTG | - |  |  | SI | (null) |
| CQUGAD | - |  |  | SI | (null) |
| CQUGAI | - |  |  | SI | (null) |
| CQULCD | - |  |  | SI | (null) |
| CQULCI | - |  |  | SI | (null) |
| CQVTRD | - |  |  | SI | (null) |
| CQVTRI | - |  |  | SI | (null) |
| ChildQ172DR | - |  |  | SI | Child Reference: Evaluación Ocular |
| Q170 | - |  |  | SI | Embarazos finalizados en los últimos 12 meses |
| Q171 | - |  |  | SI | IMC (Ind) |
| Q171ObsDR | - |  |  | SI | IMC (Ind) DR |
| Q174 | - |  |  | SI | Microalb Cuantitativa Valor |
| Q174ObsDR | - |  |  | SI | Microalb Cuantitativa Valor DR |
| QAB | - |  |  | SI | Abortos |
| QACTF | - |  |  | SI | Actividad Física |
| QACV | - |  |  | SI | ACV |
| QADI | - |  |  | SI | Ajustar dosis de Insulina |
| QAGVI | - |  |  | SI | Agudeza Visual (con corrección) Ojo Izq. |
| QALAB | - |  |  | SI | Ausentismo laboral (N° días / año) |
| QAMBT | - |  |  | SI | Amputación debajo tobillo |
| QAMST | - |  |  | SI | Amputación sobre tobillo |
| QANG | - |  |  | SI | Angor |
| QANGL | - |  |  | SI | Análogos |
| QATMP | - |  |  | SI | Atencion Médica Parcial |
| QATMT | - |  |  | SI | Atención Médica Total |
| QAVGD | - |  |  | SI | Agudeza Visual (con corrección) Ojo Der. |
| QBGD | - |  |  | SI | Biguanidas |
| QBLA | - |  |  | SI | Bloq. Alfa |
| QBLB | - |  |  | SI | Bloq. Beta |
| QBLC | - |  |  | SI | Bloq. Cálcicos |
| QBOMB | - |  |  | SI | Bomba |
| QBRAG | - |  |  | SI | Bloq. Recep. Angiotensina |
| QBYAD | - |  |  | SI | Bypass / Angioplastía derecha |
| QBYAI | - |  |  | SI | Bypass / Angioplastía izquierda |
| QC1DT | - |  |  | SI | Cetonuria Dispone de tiras |
| QC1VPS | - |  |  | SI | Cetonuria N° de Veces por semana |
| QCAD | - |  |  | SI | Cadera (cm) |
| QCATD | - |  |  | SI | Cataratas Derecha |
| QCATI | - |  |  | SI | Cataratas Izquierda |
| QCD | - |  |  | SI | Cigarrillos x día |
| QCG | - |  |  | SI | Ceguera |
| QCH1 | - |  |  | SI | 1.- Causa de hospitalizaciones |
| QCH2 | - |  |  | SI | 2.- Causa de hospitalizaciones |
| QCH3 | - |  |  | SI | 3.- Causa de hospitalizaciones |
| QCHD1 | - |  |  | SI | días 1 |
| QCHD2 | - |  |  | SI | días 2 |
| QCHD3 | - |  |  | SI | días 3 |
| QCL | - |  |  | SI | Colesterol |
| QCL1 | - |  |  | SI | Cual? |
| QCL2 | - |  |  | SI | Anal. Cual? |
| QCLL | - |  |  | SI | Callos |
| QCLV | - |  |  | SI | Colesterol Valor (mg/dl) |
| QCLVObsDR | - |  |  | SI | Colesterol Valor (mg/dl) DR |
| QCMH | - |  |  | SI | Coma hipermoslar |
| QCMI | - |  |  | SI | Claudicación miembros inferiores |
| QCMT | - |  |  | SI | Conoce sus metas de tratamiento? |
| QCPIS | - |  |  | SI | Cardiopatía isquémica |
| QCRT | - |  |  | SI | Creatinina |
| QCRTV | - |  |  | SI | Creatinina Valor (mg/dl) |
| QCRTVObsDR | - |  |  | SI | Creatinina Valor (mg/dl) DR |
| QCS | - |  |  | SI | Cesáreas |
| QCT | - |  |  | SI | Cintura (cm) |
| QCTC | - |  |  | SI | Cetoacidosis / coma |
| QCTObsDR | - |  |  | SI | Cintura (cm) DR |
| QCUP | - |  |  | SI | Cuidar los pies |
| QDD | - |  |  | SI | Deformado |
| QDFE | - |  |  | SI | Disfunción eréctil |
| QDIAT | - |  |  | SI | Dialisis / Trasplante |
| QDIUR | - |  |  | SI | Diuréticos |
| QDTS | - |  |  | SI | Dieta solamente |
| QED | - |  |  | SI | Edad al Diagnóstico |
| QEOUA | - |  |  | SI | Exámen Ojos último año |
| QEPUA | - |  |  | SI | Examen Pies último año |
| QESTA | - |  |  | SI | Estatinas |
| QFBR | - |  |  | SI | Fibratos |
| QFCCD | - |  |  | SI | Fotocoagulación Derecha |
| QFCCI | - |  |  | SI | Fotocoagulación Izquierda |
| QFSR | - |  |  | SI | Fisuras |
| QG1DT | - |  |  | SI | Glucemia Dispone de tiras |
| QG1VPS | - |  |  | SI | Glucemia N° de veces por semana |
| QG2DT | - |  |  | SI | Glucosuria Dispone de tiras |
| QG2VPS | - |  |  | SI | Glucosuria N° de Veces por semana |
| QGLA | - |  |  | SI | Glicemia ayunas (mg/dl) |
| QGLAObsDR | - |  |  | SI | Glicemia ayunas (mg/dl) DR |
| QGLC | - |  |  | SI | Glicemia casual (mg/dl) |
| QGLCD | - |  |  | SI | Glaucoma Derecha |
| QGLCI | - |  |  | SI | Glaucoma Izquierda |
| QGPS | - |  |  | SI | g x semana |
| QHB | - |  |  | SI | HBA1c |
| QHB1 | - |  |  | SI | HbA1 |
| QHB1R | - |  |  | SI | HbA1 V. referencia (Ref. Max.) (%) |
| QHB1V | - |  |  | SI | HbA1 Valor (%) |
| QHBV | - |  |  | SI | HbA1c Valor (%) |
| QHBVObsDR | - |  |  | SI | HbA1c Valor (%) DR |
| QHBVR | - |  |  | SI | HbA1c V. referencia (Ref. Max) (%) |
| QHDL | - |  |  | SI | HDL |
| QHDLV | - |  |  | SI | HDL Valor (mg/dl) |
| QHDLVObsDR | - |  |  | SI | HDL Valor (mg/dl) DR |
| QHPAO | - |  |  | SI | Hipo PA ortostática |
| QHPGS | - |  |  | SI | Hipoglicemias severas |
| QHPP | - |  |  | SI | Hosptalizaciones Parcial |
| QHPT | - |  |  | SI | Hospitalizaciones Total |
| QIAM | - |  |  | SI | IAM |
| QIBC | - |  |  | SI | Insulina Bovina Cristalina (Unid/dia) |
| QIBL | - |  |  | SI | Insulina Bovina Lenta o ultralenta (unid/dia) |
| QIBN | - |  |  | SI | Insulina Bovina NPH (unid/dia) |
| QIC | - |  |  | SI | Inicio Comprimidos (Año) |
| QICC | - |  |  | SI | I. c. c. |
| QIDTH | - |  |  | SI | Identificar / tratar hipoglicemia |
| QIECA | - |  |  | SI | Inh. ECA |
| QIGLS | - |  |  | SI | Inh. Glucosidasas |
| QIHC | - |  |  | SI | Insulina Humana Cristalina (unid/dia) |
| QIHLE | - |  |  | SI | Insulina Humana Lenta o ultralenta (unid/dia) |
| QIHN | - |  |  | SI | Insulina Humana NPH (unid/dia) |
| QII | - |  |  | SI | Inicio Insulina (Año) |
| QIMC | - |  |  | SI | IMC |
| QINFC | - |  |  | SI | Infección |
| QINSC | - |  |  | SI | Insuficiencia Cardiaca |
| QIPC | - |  |  | SI | Insulina Porcina Cristalina (unid/dia) |
| QIPLE | - |  |  | SI | Insulina Porcina Lenta o ultralenta (unid/dia) |
| QIPN | - |  |  | SI | Insulina Porcina NPH (unid/dia) |
| QLABP | - |  |  | SI | Laboratorio Parcial |
| QLABT | - |  |  | SI | Laboratorio Total |
| QLDL | - |  |  | SI | LDL |
| QLDLV | - |  |  | SI | LDL Valor (mg/dl) |
| QLDLVObsDR | - |  |  | SI | LDL Valor (mg/dl) DR |
| QMACT | - |  |  | SI | Microalb. Cuantitativa |
| QMACTV | - |  |  | SI | Microalb. Cuantitativa Valor |
| QMACTVObsDR | - |  |  | SI | Microalb. Cuantitativa Valor DR |
| QMACTVT | - |  |  | SI | Microalb. Cuantitativa (Tipo de Valor) |
| QMC | - |  |  | SI | Microalb. Cualitativa |
| QMCPD | - |  |  | SI | Maculopatía Derecha |
| QMCPI | - |  |  | SI | Maculopatía Izquierda |
| QMDCP | - |  |  | SI | Medicamentos Parcial |
| QMDCT | - |  |  | SI | Medicamentos Total |
| QMF | - |  |  | SI | Malformaciones |
| QMGLT | - |  |  | SI | Meglitidinas |
| QMP | - |  |  | SI | Muertes perinatales |
| QNCU12 | - |  |  | SI | Numero de Consultas en los últimos 12 meses |
| QNERP | - |  |  | SI | Neuropatía |
| QNEUP | - |  |  | SI | Neuropatía periférica |
| QNFP | - |  |  | SI | Nefropatía |
| QNFRP | - |  |  | SI | Nefropatía |
| QNIYD | - |  |  | SI | N° inyecciones por día |
| QOH | - |  |  | SI | Alcohol |
| QOTR1 | - |  |  | SI | Otro |
| QOTR2 | - |  |  | SI | Otros |
| QOTR3 | - |  |  | SI | Otros. |
| QOTR4 | - |  |  | SI | Otra |
| QPAD | - |  |  | SI | PA Diastólica |
| QPADObsDR | - |  |  | SI | PA Diastólica DR |
| QPAN | - |  |  | SI | Peso al nacer (Kg) |
| QPANObsDR | - |  |  | SI | Peso al nacer (Kg) DR |
| QPAS | - |  |  | SI | PA Sistólica |
| QPASObsDR | - |  |  | SI | PA Sistólica DR |
| QPEN | - |  |  | SI | PEN |
| QPER1 | - |  |  | SI | Porcentaje |
| QPER2 | - |  |  | SI | / |
| QPMCL | - |  |  | SI | Premezclada |
| QPN | - |  |  | SI | Partos Normales |
| QPPAD | - |  |  | SI | Pulso Pedio Ausente Derecho |
| QPPAI | - |  |  | SI | Pulso Pedio Ausente Izquierdo |
| QPRT | - |  |  | SI | Proteinuria |
| QPRTV | - |  |  | SI | Proteinuria Valor (g/día) |
| QPRTVObsDR | - |  |  | SI | Proteinuria Valor (g/día) DR |
| QPS | - |  |  | SI | Peso (Kg) |
| QPSC | - |  |  | SI | Piel Seca |
| QPSObsDR | - |  |  | SI | Peso (Kg) DR |
| QRAAD | - |  |  | SI | Ref. aquileano ausente derecho |
| QRAAI | - |  |  | SI | Ref. aquileano ausente izquierdo |
| QRMAD | - |  |  | SI | Resp. monofilamento anormal derecho |
| QRMAI | - |  |  | SI | Resp. monofilamento anormal izquierdo |
| QRPNPD | - |  |  | SI | Retinopatía No Proliferativa Derecha |
| QRPNPI | - |  |  | SI | Retinopatía No Proliferativa Izquierda |
| QRPP1D | - |  |  | SI | Retinopatía Preproliferativa Derecha |
| QRPP1I | - |  |  | SI | Retinopatía Preproliferativa Izquierda |
| QRVC | - |  |  | SI | Revascularización |
| QSAL | - |  |  | SI | Seleccionar Alimentos |
| QSFL | - |  |  | SI | Sulfonilureas |
| QSVAD | - |  |  | SI | Sensib. vibrat. anormal derecha |
| QSVAI | - |  |  | SI | Sensib. vibrat. anormal izquierda |
| QTB | - |  |  | SI | Tabaquismo |
| QTDM | - |  |  | SI | Tipo de Diabetes |
| QTG | - |  |  | SI | TG |
| QTGV | - |  |  | SI | TG Valor (mg/dl) |
| QTGVObsDR | - |  |  | SI | TG Valor (mg/dl) DR |
| QTIRP | - |  |  | SI | Tiras Parcial |
| QTIRT | - |  |  | SI | Tiras Total |
| QTLL | - |  |  | SI | Talla (cm) |
| QTLLObsDR | - |  |  | SI | Talla (cm) DR |
| QTZDN | - |  |  | SI | Tiazolidinedionas |
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
| QUGAD | - |  |  | SI | Úlcera / grangrena aguda derecha |
| QUGAI | - |  |  | SI | Úlcera / grangrena aguda izquierda |
| QULCD | - |  |  | SI | Úlcera curada derecha |
| QULCI | - |  |  | SI | Úlcera curada izquierda |
| QVTRD | - |  |  | SI | Vitrectomía Derecha |
| QVTRI | - |  |  | SI | Vitrectomía Izquierda |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*