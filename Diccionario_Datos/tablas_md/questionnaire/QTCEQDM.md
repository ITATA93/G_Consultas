# questionnaire.QTCEQDM

> Qualidiab

**Schema:** questionnaire
**Columnas:** 270
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Qualidiab)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQBYAD | varchar |  |  | SI | - |
| CQBYAI | varchar |  |  | SI | - |
| CQCATD | varchar |  |  | SI | - |
| CQCATI | varchar |  |  | SI | - |
| CQCL | varchar |  |  | SI | - |
| CQCRT | varchar |  |  | SI | - |
| CQFCCD | varchar |  |  | SI | - |
| CQFCCI | varchar |  |  | SI | - |
| CQGLCD | varchar |  |  | SI | - |
| CQGLCI | varchar |  |  | SI | - |
| CQHB | varchar |  |  | SI | - |
| CQHB1 | varchar |  |  | SI | - |
| CQHDL | varchar |  |  | SI | - |
| CQLDL | varchar |  |  | SI | - |
| CQMACT | varchar |  |  | SI | - |
| CQMACTVT | varchar |  |  | SI | - |
| CQMC | varchar |  |  | SI | - |
| CQMCPD | varchar |  |  | SI | - |
| CQMCPI | varchar |  |  | SI | - |
| CQPPAD | varchar |  |  | SI | - |
| CQPPAI | varchar |  |  | SI | - |
| CQPRT | varchar |  |  | SI | - |
| CQRAAD | varchar |  |  | SI | - |
| CQRAAI | varchar |  |  | SI | - |
| CQRMAD | varchar |  |  | SI | - |
| CQRMAI | varchar |  |  | SI | - |
| CQRPNPD | varchar |  |  | SI | - |
| CQRPNPI | varchar |  |  | SI | - |
| CQRPP1D | varchar |  |  | SI | - |
| CQRPP1I | varchar |  |  | SI | - |
| CQSVAD | varchar |  |  | SI | - |
| CQSVAI | varchar |  |  | SI | - |
| CQTDM | varchar |  |  | SI | - |
| CQTG | varchar |  |  | SI | - |
| CQUGAD | varchar |  |  | SI | - |
| CQUGAI | varchar |  |  | SI | - |
| CQULCD | varchar |  |  | SI | - |
| CQULCI | varchar |  |  | SI | - |
| CQVTRD | varchar |  |  | SI | - |
| CQVTRI | varchar |  |  | SI | - |
| Q170 | varchar |  |  | SI | Embarazos finalizados en los últimos 12 meses |
| Q171 | varchar |  |  | SI | IMC (Ind) |
| Q171ObsDR | varchar |  | FK | SI | IMC (Ind) DR |
| Q174 | varchar |  |  | SI | Microalb Cuantitativa Valor |
| Q174ObsDR | varchar |  | FK | SI | Microalb Cuantitativa Valor DR |
| QAB | bit |  |  | SI | Abortos |
| QACTF | varchar |  |  | SI | Actividad Física |
| QACV | varchar |  |  | SI | ACV |
| QADI | varchar |  |  | SI | Ajustar dosis de Insulina |
| QAGVI | varchar |  |  | SI | Agudeza Visual (con corrección) Ojo Izq. |
| QALAB | varchar |  |  | SI | Ausentismo laboral (N° días / año) |
| QAMBT | varchar |  |  | SI | Amputación debajo tobillo |
| QAMST | varchar |  |  | SI | Amputación sobre tobillo |
| QANG | varchar |  |  | SI | Angor |
| QANGL | varchar |  |  | SI | Análogos |
| QATMP | varchar |  |  | SI | Atencion Médica Parcial |
| QATMT | varchar |  |  | SI | Atención Médica Total |
| QAVGD | varchar |  |  | SI | Agudeza Visual (con corrección) Ojo Der. |
| QBGD | varchar |  |  | SI | Biguanidas |
| QBLA | varchar |  |  | SI | Bloq. Alfa |
| QBLB | varchar |  |  | SI | Bloq. Beta |
| QBLC | varchar |  |  | SI | Bloq. Cálcicos |
| QBOMB | bit |  |  | SI | Bomba |
| QBRAG | varchar |  |  | SI | Bloq. Recep. Angiotensina |
| QBYAD | varchar |  |  | SI | Bypass / Angioplastía derecha |
| QBYAI | varchar |  |  | SI | Bypass / Angioplastía izquierda |
| QC1DT | varchar |  |  | SI | Cetonuria Dispone de tiras |
| QC1VPS | numeric |  |  | SI | Cetonuria N° de Veces por semana |
| QCAD | numeric |  |  | SI | Cadera (cm) |
| QCATD | varchar |  |  | SI | Cataratas Derecha |
| QCATI | varchar |  |  | SI | Cataratas Izquierda |
| QCD | numeric |  |  | SI | Cigarrillos x día |
| QCG | varchar |  |  | SI | Ceguera |
| QCH1 | varchar |  |  | SI | 1.- Causa de hospitalizaciones |
| QCH2 | varchar |  |  | SI | 2.- Causa de hospitalizaciones |
| QCH3 | varchar |  |  | SI | 3.- Causa de hospitalizaciones |
| QCHD1 | varchar |  |  | SI | días 1 |
| QCHD2 | varchar |  |  | SI | días 2 |
| QCHD3 | varchar |  |  | SI | días 3 |
| QCL | varchar |  |  | SI | Colesterol |
| QCL1 | varchar |  |  | SI | Cual? |
| QCL2 | varchar |  |  | SI | Anal. Cual? |
| QCLL | varchar |  |  | SI | Callos |
| QCLV | varchar |  |  | SI | Colesterol Valor (mg/dl) |
| QCLVObsDR | varchar |  | FK | SI | Colesterol Valor (mg/dl) DR |
| QCMH | varchar |  |  | SI | Coma hipermoslar |
| QCMI | varchar |  |  | SI | Claudicación miembros inferiores |
| QCMT | varchar |  |  | SI | Conoce sus metas de tratamiento? |
| QCPIS | varchar |  |  | SI | Cardiopatía isquémica |
| QCRT | varchar |  |  | SI | Creatinina |
| QCRTV | varchar |  |  | SI | Creatinina Valor (mg/dl) |
| QCRTVObsDR | varchar |  | FK | SI | Creatinina Valor (mg/dl) DR |
| QCS | bit |  |  | SI | Cesáreas |
| QCT | varchar |  |  | SI | Cintura (cm) |
| QCTC | varchar |  |  | SI | Cetoacidosis / coma |
| QCTObsDR | varchar |  | FK | SI | Cintura (cm) DR |
| QCUP | varchar |  |  | SI | Cuidar los pies |
| QDD | varchar |  |  | SI | Deformado |
| QDFE | varchar |  |  | SI | Disfunción eréctil |
| QDIAT | varchar |  |  | SI | Dialisis / Trasplante |
| QDIUR | varchar |  |  | SI | Diuréticos |
| QDTS | varchar |  |  | SI | Dieta solamente |
| QED | numeric |  |  | SI | Edad al Diagnóstico |
| QEOUA | varchar |  |  | SI | Exámen Ojos último año |
| QEPUA | varchar |  |  | SI | Examen Pies último año |
| QESTA | varchar |  |  | SI | Estatinas |
| QFBR | varchar |  |  | SI | Fibratos |
| QFCCD | varchar |  |  | SI | Fotocoagulación Derecha |
| QFCCI | varchar |  |  | SI | Fotocoagulación Izquierda |
| QFSR | varchar |  |  | SI | Fisuras |
| QG1DT | varchar |  |  | SI | Glucemia Dispone de tiras |
| QG1VPS | numeric |  |  | SI | Glucemia N° de veces por semana |
| QG2DT | varchar |  |  | SI | Glucosuria Dispone de tiras |
| QG2VPS | numeric |  |  | SI | Glucosuria N° de Veces por semana |
| QGLA | varchar |  |  | SI | Glicemia ayunas (mg/dl) |
| QGLAObsDR | varchar |  | FK | SI | Glicemia ayunas (mg/dl) DR |
| QGLC | varchar |  |  | SI | Glicemia casual (mg/dl) |
| QGLCD | varchar |  |  | SI | Glaucoma Derecha |
| QGLCI | varchar |  |  | SI | Glaucoma Izquierda |
| QGPS | numeric |  |  | SI | g x semana |
| QHB | varchar |  |  | SI | HBA1c |
| QHB1 | varchar |  |  | SI | HbA1 |
| QHB1R | numeric |  |  | SI | HbA1 V. referencia (Ref. Max.) (%) |
| QHB1V | numeric |  |  | SI | HbA1 Valor (%) |
| QHBV | varchar |  |  | SI | HbA1c Valor (%) |
| QHBVObsDR | varchar |  | FK | SI | HbA1c Valor (%) DR |
| QHBVR | numeric |  |  | SI | HbA1c V. referencia (Ref. Max) (%) |
| QHDL | varchar |  |  | SI | HDL |
| QHDLV | varchar |  |  | SI | HDL Valor (mg/dl) |
| QHDLVObsDR | varchar |  | FK | SI | HDL Valor (mg/dl) DR |
| QHPAO | varchar |  |  | SI | Hipo PA ortostática |
| QHPGS | varchar |  |  | SI | Hipoglicemias severas |
| QHPP | varchar |  |  | SI | Hosptalizaciones Parcial |
| QHPT | varchar |  |  | SI | Hospitalizaciones Total |
| QIAM | varchar |  |  | SI | IAM |
| QIBC | varchar |  |  | SI | Insulina Bovina Cristalina (Unid/dia) |
| QIBL | varchar |  |  | SI | Insulina Bovina Lenta o ultralenta (unid/dia) |
| QIBN | varchar |  |  | SI | Insulina Bovina NPH (unid/dia) |
| QIC | numeric |  |  | SI | Inicio Comprimidos (Año) |
| QICC | varchar |  |  | SI | I. c. c. |
| QIDTH | varchar |  |  | SI | Identificar / tratar hipoglicemia |
| QIECA | varchar |  |  | SI | Inh. ECA |
| QIGLS | varchar |  |  | SI | Inh. Glucosidasas |
| QIHC | varchar |  |  | SI | Insulina Humana Cristalina (unid/dia) |
| QIHLE | varchar |  |  | SI | Insulina Humana Lenta o ultralenta (unid/dia) |
| QIHN | varchar |  |  | SI | Insulina Humana NPH (unid/dia) |
| QII | numeric |  |  | SI | Inicio Insulina (Año) |
| QIMC | varchar |  |  | SI | IMC |
| QINFC | varchar |  |  | SI | Infección |
| QINSC | varchar |  |  | SI | Insuficiencia Cardiaca |
| QIPC | varchar |  |  | SI | Insulina Porcina Cristalina (unid/dia) |
| QIPLE | varchar |  |  | SI | Insulina Porcina Lenta o ultralenta (unid/dia) |
| QIPN | varchar |  |  | SI | Insulina Porcina NPH (unid/dia) |
| QLABP | varchar |  |  | SI | Laboratorio Parcial |
| QLABT | varchar |  |  | SI | Laboratorio Total |
| QLDL | varchar |  |  | SI | LDL |
| QLDLV | varchar |  |  | SI | LDL Valor (mg/dl) |
| QLDLVObsDR | varchar |  | FK | SI | LDL Valor (mg/dl) DR |
| QMACT | varchar |  |  | SI | Microalb. Cuantitativa |
| QMACTV | varchar |  |  | SI | Microalb. Cuantitativa Valor |
| QMACTVObsDR | varchar |  | FK | SI | Microalb. Cuantitativa Valor DR |
| QMACTVT | varchar |  |  | SI | Microalb. Cuantitativa (Tipo de Valor) |
| QMC | varchar |  |  | SI | Microalb. Cualitativa |
| QMCPD | varchar |  |  | SI | Maculopatía Derecha |
| QMCPI | varchar |  |  | SI | Maculopatía Izquierda |
| QMDCP | varchar |  |  | SI | Medicamentos Parcial |
| QMDCT | varchar |  |  | SI | Medicamentos Total |
| QMF | bit |  |  | SI | Malformaciones |
| QMGLT | varchar |  |  | SI | Meglitidinas |
| QMP | bit |  |  | SI | Muertes perinatales |
| QNCU12 | varchar |  |  | SI | Numero de Consultas en los últimos 12 meses |
| QNERP | varchar |  |  | SI | Neuropatía |
| QNEUP | varchar |  |  | SI | Neuropatía periférica |
| QNFP | varchar |  |  | SI | Nefropatía |
| QNFRP | varchar |  |  | SI | Nefropatía |
| QNIYD | varchar |  |  | SI | N° inyecciones por día |
| QOH | varchar |  |  | SI | Alcohol |
| QOTR1 | varchar |  |  | SI | Otro |
| QOTR2 | varchar |  |  | SI | Otros |
| QOTR3 | varchar |  |  | SI | Otros. |
| QOTR4 | varchar |  |  | SI | Otra |
| QPAD | varchar |  |  | SI | PA Diastólica |
| QPADObsDR | varchar |  | FK | SI | PA Diastólica DR |
| QPAN | varchar |  |  | SI | Peso al nacer (Kg) |
| QPANObsDR | varchar |  | FK | SI | Peso al nacer (Kg) DR |
| QPAS | varchar |  |  | SI | PA Sistólica |
| QPASObsDR | varchar |  | FK | SI | PA Sistólica DR |
| QPEN | bit |  |  | SI | PEN |
| QPER1 | varchar |  |  | SI | Porcentaje |
| QPER2 | varchar |  |  | SI | /  |
| QPMCL | varchar |  |  | SI | Premezclada |
| QPN | bit |  |  | SI | Partos Normales |
| QPPAD | varchar |  |  | SI | Pulso Pedio Ausente Derecho |
| QPPAI | varchar |  |  | SI | Pulso Pedio Ausente Izquierdo |
| QPRT | varchar |  |  | SI | Proteinuria |
| QPRTV | varchar |  |  | SI | Proteinuria Valor (g/día) |
| QPRTVObsDR | varchar |  | FK | SI | Proteinuria Valor (g/día) DR |
| QPS | varchar |  |  | SI | Peso (Kg) |
| QPSC | varchar |  |  | SI | Piel Seca |
| QPSObsDR | varchar |  | FK | SI | Peso (Kg) DR |
| QRAAD | varchar |  |  | SI | Ref. aquileano ausente derecho |
| QRAAI | varchar |  |  | SI | Ref. aquileano ausente izquierdo |
| QRMAD | varchar |  |  | SI | Resp. monofilamento anormal derecho |
| QRMAI | varchar |  |  | SI | Resp. monofilamento anormal izquierdo |
| QRPNPD | varchar |  |  | SI | Retinopatía No Proliferativa Derecha |
| QRPNPI | varchar |  |  | SI | Retinopatía No Proliferativa Izquierda |
| QRPP1D | varchar |  |  | SI | Retinopatía Preproliferativa Derecha |
| QRPP1I | varchar |  |  | SI | Retinopatía Preproliferativa Izquierda |
| QRVC | varchar |  |  | SI | Revascularización |
| QSAL | varchar |  |  | SI | Seleccionar Alimentos |
| QSFL | varchar |  |  | SI | Sulfonilureas |
| QSVAD | varchar |  |  | SI | Sensib. vibrat. anormal derecha |
| QSVAI | varchar |  |  | SI | Sensib. vibrat. anormal izquierda |
| QTB | varchar |  |  | SI | Tabaquismo |
| QTDM | varchar |  |  | SI | Tipo de Diabetes |
| QTG | varchar |  |  | SI | TG |
| QTGV | varchar |  |  | SI | TG Valor (mg/dl) |
| QTGVObsDR | varchar |  | FK | SI | TG Valor (mg/dl) DR |
| QTIRP | varchar |  |  | SI | Tiras Parcial |
| QTIRT | varchar |  |  | SI | Tiras Total |
| QTLL | varchar |  |  | SI | Talla (cm) |
| QTLLObsDR | varchar |  | FK | SI | Talla (cm) DR |
| QTZDN | varchar |  |  | SI | Tiazolidinedionas |
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
| QUGAD | varchar |  |  | SI | Úlcera / grangrena aguda derecha |
| QUGAI | varchar |  |  | SI | Úlcera / grangrena aguda izquierda |
| QULCD | varchar |  |  | SI | Úlcera curada derecha |
| QULCI | varchar |  |  | SI | Úlcera curada izquierda |
| QVTRD | varchar |  |  | SI | Vitrectomía Derecha |
| QVTRI | varchar |  |  | SI | Vitrectomía Izquierda |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*