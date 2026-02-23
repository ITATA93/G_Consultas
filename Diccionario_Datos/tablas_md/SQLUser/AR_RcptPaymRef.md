# SQLUser.AR_RcptPaymRef

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYMREF_ParRef | bigint | PK |  | NO | AR_Receipts Parent Reference |
| ChildQ57DR | - |  |  | SI | Child Reference: Tabla Fármaco Otros |
| PAYMREF_AllocatedAmount | double |  |  | SI | Allocated Amount |
| PAYMREF_Childsub | double |  |  | NO | Childsub |
| PAYMREF_PaymentRef_DR | bigint |  | FK | SI | Des Ref to ARPaymentRef |
| PAYMREF_RowId | varchar |  |  | NO | - |
| Q42Q1 | - |  |  | SI | Reacción Adversa |
| Q42Q2 | - |  |  | SI | Fecha Inicio RAM* |
| Q42Q3 | - |  |  | SI | Duración de la RAM (Cantidad) |
| Q42Q4 | - |  |  | SI | Unidad de Tiempo |
| Q42Q5 | - |  |  | SI | Reacción Adversa |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*