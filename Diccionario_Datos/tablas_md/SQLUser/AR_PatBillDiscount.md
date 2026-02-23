# SQLUser.AR_PatBillDiscount

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISC_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| ChildQ08DR | - |  |  | SI | Child Reference: Dispositivos Gastrointestinales |
| DISC_AccountPeriod_DR | bigint |  | FK | SI | Des Ref AccountPeriod |
| DISC_Childsub | double |  |  | NO | Childsub |
| DISC_CommentDisc | varchar |  |  | SI | Comment Discount |
| DISC_Date | date |  |  | SI | Date |
| DISC_DepartDisc | varchar |  |  | SI | Department Disc |
| DISC_DiscType_DR | bigint |  | FK | SI | Des Ref DiscType |
| DISC_Discret | varchar |  |  | SI | Discretionary Discount (Discount not Payment Disco... |
| DISC_DiscretAmt | double |  |  | SI | Discret Amt |
| DISC_EmplNameDisc | varchar |  |  | SI | Empl Name Disc |
| DISC_RowId | varchar |  |  | NO | - |
| DISC_Text1 | varchar |  |  | SI | Text1 |
| DISC_Text2 | varchar |  |  | SI | Text2 |
| DISC_Time | time |  |  | SI | Time |
| DISC_User_DR | bigint |  | FK | SI | Des Ref User |
| Q07Q1 | - |  |  | SI | Tipo Dispositivo |
| Q07Q2 | - |  |  | SI | Subtipo |
| Q07Q3 | - |  |  | SI | Actividad |
| Q07Q4 | - |  |  | SI | Tamaño |
| Q07Q5 | - |  |  | SI | Ubicación |
| Q07Q6 | - |  |  | SI | N° Días Dispositivo Vía Aérea |
| Q07Q7 | - |  |  | SI | ¿Es necesario el DI? |
| Q07Q8 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*