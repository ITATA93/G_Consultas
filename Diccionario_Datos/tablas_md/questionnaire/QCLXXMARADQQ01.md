# questionnaire.QCLXXMARADQQ01

> Marcas Administrativas de Cuentas : Lista de Marcas para un Episodio

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Marcas Administrativas de Cuentas : Lista de Marcas para un Episodio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | date |  |  | SI | Fecha de Ingreso |
| Q01Q2 | time |  |  | SI | Hora de Ingreso |
| Q01Q3 | varchar |  |  | SI | Tipo de Marca |
| Q01Q4 | varchar |  |  | SI | Estado |
| Q01Q5 | varchar |  |  | SI | Comentario |
| Q01Q6 | varchar |  |  | SI | Usuario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*